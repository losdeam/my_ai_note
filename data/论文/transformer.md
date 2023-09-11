看李沐的视频进行入门[Transformer论文逐段精读【论文精读】](https://www.bilibili.com/video/BV1pu411o7BE/?spm_id_from=333.337.search-card.all.click&vd_source=3b0e33a626cf5e45835cac5d91093908)


编码器一次性看到全局进行输出，解码器一个一个的输出，并且之前的输出同样会作为后一状态的输入（自回归)
编码部分：



为什么使用layernorm而不是 batchNorm：
![Alt text](image.png)
简单理解，batchNOrm是竖着切，受样本长度影响大，如果样本长度不均匀，同时也会影响到全局方差以及平均值，而layernorm是横着切，局部的方差以及平均值仅是单样本的，受样本长度影响小。

解码部分：
受注意力机制影响，


注意力机制：

