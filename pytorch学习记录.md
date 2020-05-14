# pytorch学习记录
## `DataLoader(num_worksers)`
>It is generally not recommended to return CUDA tensors in multi-process loading because of many subtleties in using CUDA and sharing CUDA tensors in multiprocessing (see [CUDA in multiprocessing](https://pytorch.org/docs/stable/notes/multiprocessing.html#multiprocessing-cuda-note)). Instead, we recommend using [automatic memory pinning](https://pytorch.org/docs/stable/data.html#memory-pinning) (i.e., setting `pin_memory=True`), which enables fast data transfer to CUDA-enabled GPUs. -by [TORCH.UTILS.DATA](https://pytorch.org/docs/stable/data.html#multi-process-data-loading)

I think it is better not to use `num_workers` but `pin_memory=True` instead.

## `nn.zero_grad(),loss.backward(),loss.backward()`

- `zero_grad` clears old gradients from the last step (otherwise you’d just accumulate the gradients from all `loss.backward()` calls).

- `loss.backward()` computes the derivative of the loss w.r.t. the parameters (or anything requiring gradients) using backpropagation.

- `opt.step()` causes the optimizer to take a step based on the gradients of the parameters.

## 调用vgg网路代码解释
[网络链接](https://blog.csdn.net/a1103688841/article/details/89383215)

## `Net.detach()` 和 `d_loss.backward(retain_graph=True)`

`detach()` is a point to stop backwad. `ratain_graph` is to ratain the graph so as to calculate gradient twice or more. in the GAN code, it works like this : d_loss.backward(retain_graph=True)  

## [`model.eval()` vs `with torch.no_grad()`](https://discuss.p   ytorch.org/t/model-eval-vs-with-torch-no-grad/19615)

## [`def __getiem__`理解](https://blog.csdn.net/happyday_d/article/details/84899314)

## [`Pytorch Module Save`](https://pytorch.org/tutorials/beginner/saving_loading_models.html?highlight=load)

## C++ Combile Pytorch

[Reference Website](https://pytorch.org/tutorials/advanced/cpp_export.html#a-minimal-c-application.I)

1. Using `zhuanhuanmoxing.py` to load *.pth* file and transfer to *.pt* file, remember to `import GeneratorNetModule`

2. Install libtorch, using two things: **example-app.cpp**, and **cmakeList**.

   **cmakeList** need *[Download libtorch]([libtorch](https://zhuanlan.zhihu.com/p/92374964)), [opencv ](https://www.zhihu.com/question/263917089)*and *[ippicv](https://www.cnblogs.com/yongy1030/p/10293178.html), torch path* is `/home/li/anaconda3/envs/py3.6/lib/python3.6/site-packages/torch/share/cmake/Torch`。这里opencv安装了一整天，就是不行。最后anaconda安装的才OK，用的

   **example-app.cpp** 其中module参考新网站，module调用方法用`.`不能用`->`, 这个cpp写的是HM要调用时的C++函数

   然后`mkdir build`， `cd build`, `cmake ..`, `make`.

   生成example-app, 之后HM里`system(PathToExample-app)；`