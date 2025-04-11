#include <SDL2/SDL.h>
#include <iostream>

// g++ frontend/main.cpp -o main -Ibuild/include/SDL2 -Dmain=SDL_main -Lbuild/lib -lmingw32 -lSDL2main -lSDL2
// ./main

// can be ran in vscode terminal

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;

int main(int argc, char* argv[])
{
	if (SDL_Init(SDL_INIT_EVERYTHING) > 0)
	{
		std::cout << "SDL_Init failed with error: " << SDL_GetError() << std::endl;
		return 1;
	}

	window = SDL_CreateWindow("Hello SDL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
	if (!window) {
		std::cout << "SDL_CreateWindow failed with error: " << SDL_GetError() << std::endl;
		return 1;
	}

	renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_PRESENTVSYNC);
    if (!renderer) {
        std::cout << "SDL_CreateRenderer failed with error: " << SDL_GetError() << std::endl;
		return 1;
    }

	std::string greetings = "Hello SDL2!";
	std::cout << greetings << std::endl;

	SDL_bool running = SDL_TRUE;
    while (running) {
        SDL_Event e;
        while (SDL_PollEvent(&e)) {
            switch (e.type) {
                case SDL_QUIT: {
                    running = SDL_FALSE;
                    break;
                }
			}
		}
	}

	SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);

    SDL_Quit();

    return 0;
}