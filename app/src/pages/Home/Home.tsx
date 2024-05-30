import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/react";
// import ExploreContainer from "../components/ExploreContainer";
import ExploreContainer from "../../components/ExploreContainer";
import {
  Button,
  ButtonGroup,
  Center,
  Icon,
  Input,
  WrapItem,
  Text,
  VStack,
} from "@chakra-ui/react";
import { Grid, GridItem } from "@chakra-ui/react";
import { Container } from "@chakra-ui/react";
import "./Home.css";
import { Search2Icon } from "@chakra-ui/icons";
// import { StaveNote, Vex } from "vexflow";
import { createElement, useEffect, useRef, useState } from "react";
import { Filesystem, Directory } from "@capacitor/filesystem";
import { FilePicker } from "@capawesome/capacitor-file-picker";
import { parseString } from "xml2js";
import { FaMusic } from "react-icons/fa";
import { Card, CardHeader, CardBody, CardFooter } from "@chakra-ui/react";
import { BsFileEarmarkMusic } from "react-icons/bs";
import HomeBody from "./HomeBody/HomeBody";
import HomeHeader from "./HomeHeader/HomeHeader";


export default function Home() {
  const [xml, setXml] = useState<any>(null);
  return (
    <IonPage>
      <IonContent fullscreen>
        <HomeHeader setXml={setXml} />
        <HomeBody xml={xml} />
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Home</IonTitle>
          </IonToolbar>
        </IonHeader>
      </IonContent>
    </IonPage>
  );
}
