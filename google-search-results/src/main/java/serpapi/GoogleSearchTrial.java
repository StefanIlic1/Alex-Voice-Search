package serpapi;
// import the google search that is in the same package
import serpapi.GoogleSearch;
import serpapi.SerpApiSearch;
import serpapi.SerpApiSearchException;

import java.io.Console;
import java.util.HashMap;
import java.util.Map;

public class GoogleSearchTrial {
    public static void main (String[] args) {
         Map<String, String> parameter = new HashMap<>();

        parameter.put("q", "Coffee");
        parameter.put("location", "Naperville, Illinois, United States");
        parameter.put("hl", "en");
        parameter.put("gl", "us");
        parameter.put("google_domain", "google.com");
        parameter.put("api_key", "2035296457b5d92d8f577ee0cc9839423d51404936d3fa7b12223dfc0cf8581d");
        
        GoogleSearch search = new GoogleSearch(parameter);
        

        try
        {
          JsonObject results = search.getJson();
        }
        catch (SerpApiClientException ex)
        {
          Console.WriteLine("Exception:");
          Console.WriteLine(ex.ToString());
        }
    }
}