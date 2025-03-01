import torch.nn as nn

class ModuleAttrMixin(nn.Module):
    def __init__(self):
        super().__init__()
        # self._dummy_variable = nn.Parameter()
        self._dummy_variable = nn.Parameter(requires_grad=False)

    @property
    def device(self):
        return next(iter(self.parameters())).device
    
    @property
    def dtype(self):
        return next(iter(self.parameters())).dtype
