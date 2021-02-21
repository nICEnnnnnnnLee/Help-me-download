<p align="center">
      <strong>
        <a href="https://github.com/ButterAndButterfly/Help-me-download" target="_blank">Help-me-download</a>&nbsp;
      </strong>
  <br>
      made by<strong>
        <a href="https://github.com/ButterAndButterfly" target="_blank">ButterAndButterfly</a><br>
      </strong>  
        Butter, symbolizes Otaku; Butterfly, symbolizes the Great things. 
        <br/> Let's earn a world full of fantasy!
</p>

[ReadMe](https://github.com/ButterAndButterfly/Help-me-download/blob/master/README.md)  [ReadMe中文版](https://github.com/ButterAndButterfly/Help-me-download/blob/master/README_CN.md)
## Fucntion
Let the github robots download the things you want, and then push it to the release assets.

## How to config
```
{
    // default headers to download
    "headers":{
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip"
    },
    // release config, it must be diffrent from the former tasks
    "release_tag": "v1.0.0",
    "release_name": "v1.0.0",
    // the name of release assets
    "output": "test.zip",
    // tasks must be a array, even with a single task
    "tasks":[
        {
            "file_name": "test-40.jpg",
            "file_url":"https://avatars.githubusercontent.com/u/52323235?s=60&v=4",
            // optional; if headers appear, the default headers will be uneffective;
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

## How to use
+ Fork/clone the project, or use this project as Template to create one
+ Enable the Github Actions Settings
+ Now you have two way to run a download task:
    + By push a commit
        + edit the `config.json`
        + commit changes and push to the repo
    + By create an issue comment
        + The content of issue comment should be something like that in `config.json`
        + The act is to reply an issue, NOT create an issue
        + Just see [issue#1](https://github.com/ButterAndButterfly/Help-me-download/issues/1)
## Notice
+ The github action bot works only for the owner of repo when issue comment created.
+ You could set the repo to private for privacy.

## LICENSE
MIT 


