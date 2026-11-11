# 第 1 天完成标志：环境验证脚本
print("Hello 多模态！")
import sys, torch, numpy, pandas, matplotlib
print(f"Python {sys.version.split()[0]} | torch {torch.__version__} | numpy {numpy.__version__}")
# 快速验证张量与自动求导
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2
y.backward()
print(f"自动求导自检: d(x^2)/dx 在 x=3 处 = {x.grad.item()}（期望 6.0）")
print("环境自检全部通过 [OK]")
# 同步实验
# 是不是每一次更新都是这个流程？我也是不知道怎么说，今天是学习到了。