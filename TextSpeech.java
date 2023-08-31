import javax.speech.Central;
import com.sun.speech.freetts.*;

public class TextSpeech
{
    public static void main(String[] args)
    {
        try 
        {

            Voice voice;
            System.setProperty("freetts.voices", "com.sun.speech.freetts.en.us.cmu_us_kal.KevinVoiceDirectory");
            Central.registerEngineCentral("com.sun.speech.freetts.jsapi.FreeTTSEngineCentral");

            voice = VoiceManager.getInstance().getVoice("kevin");
            voice.allocate();
            voice.speak("hello my name is alex heeheehoohoo");
            voice.deallocate();
        } 
        
        catch (Exception e)
        {
            System.out.print(e);
        }
    }
}