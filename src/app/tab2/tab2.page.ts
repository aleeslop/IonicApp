import { Component } from '@angular/core';
import { IonAccordion, IonAccordionGroup, IonItem, IonLabel,IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/angular/standalone';
import { ExploreContainerComponent } from '../explore-container/explore-container.component';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss'],
  imports: [IonAccordion, IonAccordionGroup, IonItem, IonLabel, IonHeader, IonToolbar, IonTitle, IonContent, ExploreContainerComponent]
})
export class Tab2Page {

  constructor() {}

}
