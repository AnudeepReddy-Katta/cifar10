from torch import nn


class SimpleDenseNet(nn.Module):
    def __init__(
        self,
        channels : int = 3,
        width : int = 32,
        height : int = 32,
        hidden_size: int = 64,

        output_size: int = 10,
    ):
        super().__init__()

        self.model = nn.Sequential(

            nn.Flatten(),
            nn.Linear(channels * width * height, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x):
        batch_size, channels, width, height = x.size()

        # (batch, 1, width, height) -> (batch, 1*width*height)
        x = x.view(batch_size, -1)

        return self.model(x)


if __name__ == "__main__":
    _ = SimpleDenseNet()
