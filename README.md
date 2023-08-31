# raspberry-pi-project

to configure your speakers for FreeTTS, copy:
javax.sound.sampled.Clip=com.sun.media.sound.DirectAudioDeviceProvider
javax.sound.sampled.Port=com.sun.media.sound.PortMixerProvider
javax.sound.sampled.SourceDataLine=com.sun.media.sound.DirectAudioDeviceProvider
javax.sound.sampled.TargetDataLine=com.sun.media.sound.DirectAudioDeviceProvider

into: 
/usr/lib/jvm/java-11-openjdk-arm64/conf/sound.properties