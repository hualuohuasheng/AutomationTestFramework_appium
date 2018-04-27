## iRoom_demo的控件

### 1、登录界面

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|ndselect输入框|enter ndSelect|com.powerinfo.pi_iroom.demo:id/mEtNdSelect|send_keys()/send_text()||
|groupid输入框|enter groupId|com.powerinfo.pi_iroom.demo:id/mEtGroupId|同上|
|域名服务器|powzamedia.com|com.powerinfo.pi_iroom.demo:id/mEtDomain|同上|一般不改|
|servermode|空|com.powerinfo.pi_iroom.demo:id/mSpServerMode|click()|默认不管|
|端口|80|com.powerinfo.pi_iroom.demo:id/mEtStartPort|send_keys()||
|start|START|com.powerinfo.pi_iroom.demo:id/mBtnStart|click()|


eg:
driver.find_element_by_id("com.powerinfo.pi_iroom.demo:id/mBtnStart").click()

### 2、权限问题
- 会连续弹出3个获取权限的框，分别是相机、麦克风和sd卡

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|始终允许|始终允许|com.android.packageinstaller:id/permission_allow_button|
|禁止|禁止|com.android.packageinstaller:id/permission_deny_button|

### 3、房间列表大厅

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|创建房间的‘+’|空|com.powerinfo.pi_iroom.demo:id/iv_create_room|
|房间号|RoomID :2481|com.powerinfo.pi_iroom.demo:id/tv_roomId|
|房间加锁标志|空|com.powerinfo.pi_iroom.demo:id/iv_lock|

### 4、加入房间界面

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|标题|Join Room 2481/Create Your New Room|com.powerinfo.pi_iroom.demo:id/tv_title|
|参数信息|336*192, 20fps, 500kbp|com.powerinfo.pi_iroom.demo:id/tv_setting_info|
|加入房间|START/JOIN|com.powerinfo.pi_iroom.demo:id/bt_start|
|房间加锁标志|空|com.powerinfo.pi_iroom.demo:id/iv_setLock|
|设置|空|com.powerinfo.pi_iroom.demo:id/iv_setting|

### 5、设置密码界面

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|标题|Please enter the password|com.powerinfo.pi_iroom.demo:id/alertTitle|
|输入框|空|空||使用class android.widget.EditText|
|确认按钮|Yes|android:id/button1|
|取消按钮|Cancel|android:id/button2|


### 6、设置界面

- 常用配置

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|设置码率Bitrate|500（显示多少就是多少）|com.powerinfo.pi_iroom.demo:id/mEtBitrate|
|帧率|空|com.powerinfo.pi_iroom.demo:id/mSpFps|click()|
|帧率选择下拉框|15/20/25|android:id/text1(3个都是)|s|class:android.widget.CheckedTextView|
|选择分辨率|空|com.powerinfo.pi_iroom.demo:id/mSpOutputSize||下拉框同上|
|观众模式|关闭|com.powerinfo.pi_iroom.demo:id/mScViewerMode|
|MSC模式|关闭|com.powerinfo.pi_iroom.demo:id/mScMscMode|
|开发者选项|Developer Options|com.powerinfo.pi_iroom.demo:id/bt_developer|
|群聊类型|空|com.powerinfo.pi_iroom.demo:id/mSpPkMode|
|美颜|空|com.powerinfo.pi_iroom.demo:id/mSpBeautifyType|
|ptcp日志|关闭|com.powerinfo.pi_iroom.demo:id/mPtcpLog|
|本地录制|Local Record|com.powerinfo.pi_iroom.demo:id/mBtnLocalRecord|
|上传日志|Upload Log|com.powerinfo.pi_iroom.demo:id/mBtnUploadLog|
|清理日志|Delete Log|com.powerinfo.pi_iroom.demo:id/mBtnDeleteLog|
|登出|Logout|com.powerinfo.pi_iroom.demo:id/mBtnLogout|



- 其它配置

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|RS超时时间|8000|com.powerinfo.pi_iroom.demo:id/mEtRSTimeoutThreshold|
|音频比特率码|48000|com.powerinfo.pi_iroom.demo:id/mEtAudioEncodeBitrate||一般默认不管|
|预览分辨率|空|com.powerinfo.pi_iroom.demo:id/mSpPreviewSize||下拉框同上，一般默认|
|音频编码类型||com.powerinfo.pi_iroom.demo:id/mSpAudioEncoderType|
|声道类型||com.powerinfo.pi_iroom.demo:id/mSpAudioChannelNum|
|音频采样率||com.powerinfo.pi_iroom.demo:id/mSpAudioSampleRate||一般默认不管|
|AEC模式||com.powerinfo.pi_iroom.demo:id/mSpAecMode|
|后台播放设置||com.powerinfo.pi_iroom.demo:id/mScStopPlayOnPause|
|tanscode模式||com.powerinfo.pi_iroom.demo:id/mSpTranscoderMode|
|后台推流设置||com.powerinfo.pi_iroom.demo:id/mSpBackgroundBehavior|
|DEV模式|关闭|com.powerinfo.pi_iroom.demo:id/mDevMode|
|EnableAvDelta Correction|关闭|com.powerinfo.pi_iroom.demo:id/mAvDeltaCorrection|
|CBR|关闭|com.powerinfo.pi_iroom.demo:id/mCbr|
|内存泄露检测leakCanary|关闭|com.powerinfo.pi_iroom.demo:id/mStartLeakCanary|


### 7、房间内界面

|控件名称|text|resource_id|方法|备注|
|---|---|---|---|---|
|房间号|RoomId:2481|com.powerinfo.pi_iroom.demo:id/tv_roomId|get_text()|
|切换摄像头|空|com.powerinfo.pi_iroom.demo:id/iv_camera|
|开关闪光灯|空|com.powerinfo.pi_iroom.demo:id/iv_torch|
|美颜|空|com.powerinfo.pi_iroom.demo:id/iv_beauty|
|切换角色|空|com.powerinfo.pi_iroom.demo:id/iv_change_role|
|合并房间|空|com.powerinfo.pi_iroom.demo:id/iv_merge_room|
|合并房间标题|Choose Actions|com.powerinfo.pi_iroom.demo:id/md_title|
|合并房间的列表|空|空|-|class：android.widget.LinearLayout，index：0/1/2...|
|取消按钮|Cancel|com.powerinfo.pi_iroom.demo:id/md_buttonDefaultNegative|
|快速加入房间|空|com.powerinfo.pi_iroom.demo:id/iv_change_room|
|退出房间|空|com.powerinfo.pi_iroom.demo:id/iv_back|
|状态信息|-|com.powerinfo.pi_iroom.demo:id/tv_info|
|打点码|-|com.powerinfo.pi_iroom.demo:id/mBtnWhoops|

