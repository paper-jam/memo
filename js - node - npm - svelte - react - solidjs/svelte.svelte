<!-- 
--- ===============  SVELTE
précompilateur WEB // Un fichier .svelte est un fichier html valide // Le code du runtime svelte est écrit en typescript
component : 3 sections : SCRIPT / STYLE / MAIN


VIDEO du DOCTEUR: REPRENDRE à 7 : gestion du click



<!-- 4 ======= User Input and Data Binding -->    -- A REPRENDRE A FINIR
<input type="text" placeholder='name' bind:value={name}>


<!-- 6 ======= boucle -->
{#each people as person (person.id)} ... {:else} ... {/each}

<!-- 7 ======= inline evnet handlers -->
<button on:click={(e) => handleClick(e, person.id)}>delete</button>

<!-- 8 ======= conditionnal -->
{#if num > 20} ... {:else if num > 5} ... {:else} ... {/if}

<!-- 9 ======= Components -->
 import Modal from './Modal.svelte';
 <Modal />

<!-- 10 ======= CSS and conditionnal styles  -->
<div class="backdrop" class:promo={isPromo}>

<!-- 11 ======= using props         -->
export let message = 'default message';              <!-- in Modal.svelte -->
<Modal message='Hello, Ninjas!' isPromo={true} />    <!-- in App.svelte --> 

<!-- -- 12 ======= Event Forwarding  -->
<div class="backdrop" class:promo={isPromo} on:click>                   <!-- in Modal.svelte -->
<Modal message='Hello, Ninjas!' {showModal} on:click={toggleModal} />   <!-- in App.svelte --> 
<button on:click={toggleModal}>Open Modal</button>                      <!-- in App.svelte -->

<!-- -- 13 ======= Event Modifiers 12h06 -->                            
<div class="backdrop" class:promo={isPromo} on:click|self>      <!-- apply only in the div and not in his children -->    
<button on:click|once={toggleModal}>Open Modal</button>         <!-- apply once -->    

<!-- -- 14 ======= Slots 12h20 --> ------ A REVOIR https://svelte.dev/tutorial/named-slots
<slot name="title">... </slot>      <!-- in Modal.svelte : names slot-->
<slot></slot>                       <!-- in Modal.svelte : -->

<!-- -- 15 ======= Forms (part 1)  -->
<form on:submit|preventDefault={handleSubmit}>

<!-- -- 16 ======= Forms (part 2) -->
let skills = [];
<input type="checkbox" bind:group={skills} value="fighting">fighting<br>
<input type="checkbox" bind:group={skills} value="fighting">fighting<br>
  <label>Belt colour:</label>
  <select bind:value={beltColour}>
    <option value="black">black</option>
    <option value="orange">orange</option>
  </select>

<!-- -- 17 ======= Dispatching Custom Events -->
let dispatch = createEventDispatcher();
dispatch('addPerson', person);

const addPerson = (e) => {...}
<AddPersonForm on:addPerson={addPerson} />
people = [person, ...people];

<!-- -- 18 ======= Starting the Polls Project   -->
<!-- -- 19 =======  Header & Footer Components  -->
CSS REVOIR : display: inline-block;

<!-- -- 20 ======= Reusable Tabs Component 10h33--> 
<!-- -- 21 ======= Poll Form Component -->
<!-- -- 22 ======= Custom Button Component->

<!-- -- 23 ======= Custom Form Validation -->
<!-- -- 24 ======= Adding New Polls       -->
<!-- -- 25 ======= -->
<!-- -- 26 ======= Card Component         -->
<!-- -- 27 ======= Casting Votes          -->
 const { id, option } = e.detail;
 let copiedPolls = [...polls];    <!-- make a copy of the array -->

<!-- -- 28 ======= Vote Bars              -->
<!-- -- 29 =======  Introduction to Stores -->
import { writable } from 'svelte/store';
PollStore.subscribe...

<!-- -- 30 ======= Lifecycle Hooks -->
life component is made of events : onMount / onDestroy / ...
import { onMount, onDestroy } from 'svelte';
onMount(() => { /* maybe get data from a db ...*/});

// no need to un/subscribe :) 
import PollStore from '../stores/pollStore.js';
#each $PollStore as poll (poll.id)

<!-- -- 31 ======= Updating store data -->
<!-- -- 32 ======= Deleting polls     -->
<!-- -- 33 ======= Transition basics  -->
Transitions are usable only on HTML elements 
import { fade, slide, scale } from 'svelte/transition';
import { flip } from 'svelte/animate';

<!-- -- 34 ======= Tweens & Animations  -->
 $: tweenedA.set(percentA);  // tweenedA est mis à jour automatiquement qd la valeur de percentA est modifiée

<!-- -- 35 ======= Wrap Up-->
sapper tutorial










