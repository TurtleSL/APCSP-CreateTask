#include <SDL2/SDL.h>
#include <iostream>

// g++ frontend/C++/main.cpp -o main -Ifrontend/include/SDL2 -Dmain=SDL_main -Lfrontend/lib -lmingw32 -lSDL2main -lSDL2
// ./main

// can be ran in vscode terminal

static SDL_Window *window = NULL;
static SDL_Renderer *renderer = NULL;

int main(int argc, char* argv[])
{
  if (SDL_Init(SDL_INIT_EVERYTHING) > 0)
  {
    std::cout << "SDL_Init failed with error: " << SDL_GetError() << std::endl;
    return EXIT_FAILURE;
  }

    window = SDL_CreateWindow("Hello SDL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);
    if (!window) {
        std::cout << "SDL_CreateWindow failed with error: " << SDL_GetError() << std::endl;
    }

  std::string greetings = "Hello SDL2!";
  std::cout << greetings << std::endl;

  SDL_Quit();

  return EXIT_SUCCESS;
}