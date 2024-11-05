#include <fuzzer/FuzzedDataProvider.h>
#include <cstdint> // For uint32_t
#include <cstring> // For memset
#include <vector>  // For std::vector

// Assuming GfxState is a defined class. Include its header if necessary.
class GfxState {
public:
    int fontSize;
    char fontName[50]; // Example for a font name

    GfxState() {
        // Initialize members
        fontSize = 12; // Default font size
        memset(fontName, 0, sizeof(fontName)); // Clear font name
    }

    void setFontSize(int size) {
        fontSize = size;
    }

    void setFontName(const char* name) {
        strncpy(fontName, name, sizeof(fontName) - 1);
        fontName[sizeof(fontName) - 1] = '\0'; // Ensure null-termination
    }
};

class SplashOutputDev {
public:
    void doUpdateFont(GfxState *state) {
        // Function implementation (placeholder)
        // This is just for demonstration and should be replaced with actual logic.
        printf("Font Size: %d, Font Name: %s\n", state->fontSize, state->fontName);
    }
};

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    FuzzedDataProvider stream(data, size);

    // Create an instance of SplashOutputDev
    SplashOutputDev splashOutputDev;

    // Create a GfxState object
    GfxState gfxState;

    // Use the fuzzed data to influence the GfxState
    int fontSize = stream.ConsumeIntegralInRange<int>(1, 100); // Random font size between 1 and 100
    gfxState.setFontSize(fontSize);

    // Consume a string from the fuzzed data for the font name
    std::string fontName = stream.ConsumeRandomLengthString(49); // Max length 49 to fit in the buffer
    gfxState.setFontName(fontName.c_str());

    // Call the function under test
    splashOutputDev.doUpdateFont(&gfxState);

    return 0;
}