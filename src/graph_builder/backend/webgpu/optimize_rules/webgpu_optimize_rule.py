from graph_builder.backend.webgpu.optimize_rules.optimize_convolution2d import OptimizeConvolution2D
from graph_builder.backend.webgpu.optimize_rules.optimize_deconvolution2d import OptimizeDeconvolution2D
from graph_builder.backend.webgpu.optimize_rules.optimize_elementwise import OptimizeElementwise
from graph_builder.graph.optimize_rule import OptimizeRule


class WebGPUOptimizeRule(OptimizeRule):
    def __init__(self):
        super(WebGPUOptimizeRule, self).__init__()

        self.register(OptimizeConvolution2D())
        self.register(OptimizeDeconvolution2D())
        self.register(OptimizeElementwise())