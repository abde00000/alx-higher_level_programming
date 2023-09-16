#ifndef DOG_H
#define DOG_H

/**
 * struct dog - infos about a dog
 * @name: name of the dog
 * @age: age of the dog
 * @owner: owner of the do
 *
 * Description: Longer description
 */

struct dog
{
	char *name;
	float age;
	char *owner;
};

/**
 * dog_t - new defined type for struct dog
 */
typedef struct dog dog_t;
void init_dog(struct dog *d, char *name, float age, char *owner);
void print_dog(struct dog *d);
dog_t *new_dog(char *name, float age, char *owner);
#endif
