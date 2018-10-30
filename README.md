# AutomationTestFramework_appium

基于appium的移动端自动化测试平台，执行测试任务，测试结果截图，生成测试报告并发送邮件

## 使用说明

- 1、在devices.yml文件中查看要进行自动化的手机相关配置，如果此文件中没有相关配置，复制模板后修改系统版本、uid即可
- 2、在iRoomtestcase.py文件中有2个class，分别为安卓和ios，更改setUp中的devicelist参数，
    将进行自动化手机添加到devicelist参数中，填入的名字为devices.yml中的配置名称 `devicelist = ['sony','meizu-pro7']`
- 3、在iRoomtestcase文件中每个class的后3个case，需要另外一台手机先创建好房间，然后把房间号修改用例中相关
    `roomxpath = re.sub("xxxx", '4021', self.控件信息['房间列表']['xpath'])`
- 4、在suite_singletest.py文件中输入要运行的test,可填入1个或多个
- 5、运行suite_singletest.py文件即可


## 需第三方库

- 1、appium的python客户端库，`pip install Appium-Python-Client`
- 2、读取yaml文件的库,`pip install pyyaml`
