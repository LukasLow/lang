#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

static size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t total_size = size * nmemb;
    strncat(userp, contents, total_size);
    return total_size;
}

void get_weather(const char *city) {
    CURL *curl;
    CURLcode res;

    char url[256];
    snprintf(url, sizeof(url), "https://wttr.in/%s?format=3", city);

    char buffer[256] = {0};

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &buffer);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
            printf("Wetter in %s: %s\n", city, buffer);
        }

        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();
}

int main() {
    char city[50];
    printf("Gib den Namen der Stadt ein: ");
    scanf("%s", city);

    get_weather(city);

    return 0;
}
