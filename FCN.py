from torchvision import models
from torch.nn import CrossEntropyLoss
from torch.optim import SGD


class FCN(torch.nn.Module):
    def __init__(self, pretrained_model=None):
        super(FullyConvNet, self).__init__()
        if pretrained_model is None:
            self.model = models.segmentation.fcn_resnet101(pretrained=True, num_classes=2, progress=True)
        else:
            self.model = pretrained_model

    def forward(self, x):
        prediction = self.model(x)['out']
        return prediction


def iou(pred, Y):
    intersection = torch.sum((pred > 0) * (Y > 0))
    union = torch.sum((pred > 0) + (Y > 0))
    return intersection.float() / union.float()


class NeuroNet:
    def __init__(self, model, optimizer=None, criterion=CrossEntropyLoss(), progress=True):
        self.model = model
        if optimizer is None:
            self.optimizer = SGD(model.parameters(), momentum=True)
        else:
            self.optimizer = optimizer
        self.criterion = criterion


    # Data is a dictionary with keys 'train','test' and values tensor [height x width x 3 x batch_size]
    def train(self, data, num_epoch=5):
        since = time.time()
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        best_model_wts = copy.deepcopy(model.state_dict())
        best_acc = 0.0
        for epoch in range(num_epoch):
            if progress is True:
                print('Epoch {}/{}'.format(epoch, num_epochs - 1))
                print('-' * 10)

            # Each epoch has a training and testing phase
            for phase in ['train', 'test']:
                if phase == 'train':
                    self.model.train()  # Set model to training mode
                else:
                    self.model.eval()  # Set model to evaluate mode

                running_loss = 0.0
                running_corrects = 0

                # Iterate over data.
                for input, output in data[phase]:
                    input = input.to(device)
                    output = output.to(device)

                    # zero the parameter gradients
                    self.optimizer.zero_grad()

                    # track history if only in train
                    with torch.set_grad_enabled(phase == 'train'):
                        predict = self.model(input)
                        loss = self.criterion(predict, output)
                        IoU = iou(predict, output)

                        # backward + optimize only if in training phase
                        if phase == 'train':
                            loss.backward()
                            self.optimizer.step()

                    # statistics
                    running_loss += loss.item() * input.size(0)
                    running_corrects += torch.sum(predict.data == output.data)
                    running_IoU += IoU * input.size(0)
                if phase == 'train':
                    scheduler.step()

                epoch_loss = running_loss / data_sizes[phase]
                epoch_acc = running_corrects.double() / data_sizes[phase]
                epoch_iou = running_iou / data_sizee[phase]

                if progress is True:
                    print('{} Loss: {:.4f} Acc: {:.4f} IoU: {:.4f} '.format(
                        phase, epoch_loss, epoch_acc, epoch_IoU))

                # deep copy the model
                if phase == 'test' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(self.model.state_dict())
            if progress is True:
                print()
        time_elapsed = time.time() - since
        if progress is True:
            print('Training complete in {:.0f}m {:.0f}s'.format(
                time_elapsed // 60, time_elapsed % 60))
            print('Best val Acc: {:4f}'.format(best_acc))

        # load best model weights
        self.model.load_state_dict(best_model_wts)
        return model

