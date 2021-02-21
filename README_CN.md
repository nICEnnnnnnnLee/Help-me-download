<p align="center">
      <strong>
        <a href="https://github.com/ButterAndButterfly/Help-me-download" target="_blank">Help-me-download</a>&nbsp;
      </strong>
  <br>
      源自<strong>
        <a href="https://github.com/ButterAndButterfly" target="_blank">ButterAndButterfly</a><br>
      </strong>  
        Butter, 寓意宅男; Butterfly, 寓意美好的事物。 
        <br/> 美好的世界由我们创造!  
</p>

[ReadMe](https://github.com/ButterAndButterfly/Help-me-download/blob/master/README.md)  [ReadMe中文版](https://github.com/ButterAndButterfly/Help-me-download/blob/master/README_CN.md)
## 功能
让GitHub机器人帮忙代下载，然后发布到release附件。

## 如何配置
```
{
    // 下载的默认headers
    "headers":{
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip"
    },
    // release 配置，不能和已有的release重复
    "release_tag": "v1.0.0",
    "release_name": "v1.0.0",
    // release 附件的名称
    "output": "test.zip",
    // 任务数组，必须是一个数组。
    "tasks":[
        {
            "file_name": "test-40.jpg",
            "file_url":"https://avatars.githubusercontent.com/u/52323235?s=60&v=4",
            // 可选。如果此处出现headers，则默认headers配置无效
            "headers":{
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, br"
            },
        },{
            "file_name": "test-60.jpg",
            "file_url":"https://avatars.githubusercontent.com/u/52323235?s=60&v=4"
        }
    ]
}
```

## 如何使用
+ fork/clone本项目，或者使用本项目模板创建一个新项目
+ 打开项目的Github Actions设置
+ 接下来你可以有两种使用方法:
    + 通过修改配置文件然后push到新的项目
        + 编辑`config.json`
        + 提交修改并push
    + 通过回复issue
        + 回复的内容和配置一致，参考`config.json`
        + 是回复issue，不是创建issue
        + 参考[issue#1](https://github.com/ButterAndButterfly/Help-me-download/issues/1)
## 注意
+ 当有问题被回复时，GitHub机器人只会处理项目拥有者的请求
+ 为了隐私需要，你可以将项目设为私有。

## LICENSE
MIT 


