import {Fragment,useCallback,useContext,useEffect} from "react"
import {Box as RadixThemesBox,Button as RadixThemesButton,Flex as RadixThemesFlex,Heading as RadixThemesHeading,Link as RadixThemesLink,Separator as RadixThemesSeparator,Text as RadixThemesText,TextArea as RadixThemesTextArea,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {Helmet} from "react-helmet"
import {Link as ReactRouterLink} from "react-router"
import {Root as RadixFormRoot} from "@radix-ui/react-form"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,getRefValue,getRefValues} from "$/utils/state"
import {jsx} from "@emotion/react"




function Root_285a8a2bf0211d711adc4e533989e89a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

    const handleSubmit_e5c71d71003d22f753e08715a3b21e4d = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(ReflexEvent("reflex___state____state.first_steps___components___form____contact_form_state.handle_submit", ({ ["form_data"] : form_data }), ({  })))], args, ({  }))))(ev));

        if (true) {
            $form.reset()
        }
    })
    


  return (
    jsx(RadixFormRoot,{className:"Root ",css:({ ["width"] : "100%" }),onSubmit:handleSubmit_e5c71d71003d22f753e08715a3b21e4d},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"column",gap:"3"},jsx(RadixThemesTextField.Root,{name:"first_name",placeholder:"Nombre"},),jsx(RadixThemesTextField.Root,{name:"last_name",placeholder:"Apellido"},),jsx(RadixThemesTextField.Root,{name:"email",placeholder:"Email",type:"email"},),jsx(RadixThemesTextArea,{css:({ ["& textarea"] : null }),name:"mensaje",placeholder:"Tu Mensaje"},),jsx(RadixThemesButton,{type:"submit"},"Enviar Consulta")))
  )
}


function Text_2071de36054a691f8c6c5caebfeec8f6 () {
  const reflex___state____state__first_steps___components___form____contact_form_state = useContext(StateContexts.reflex___state____state__first_steps___components___form____contact_form_state)



  return (
    jsx(RadixThemesText,{as:"p"},(JSON.stringify(reflex___state____state__first_steps___components___form____contact_form_state.form_data_rx_state_)))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{css:({ ["backgroundImage"] : "linear-gradient(to top, #000, #31175e)", ["minHeight"] : "100vh", ["display"] : "grid" })},jsx(Fragment,{},jsx(Helmet,{},jsx("script",{},"document.documentElement.lang='es'"))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["zIndex"] : "999", ["background"] : "#31175e", ["paddingLeft"] : "0.625rem", ["paddingRight"] : "0.625rem", ["display"] : "flex", ["@media screen and (min-width: 0)"] : ({ ["justifyContent"] : "space-around" }), ["@media screen and (min-width: 30em)"] : ({ ["justifyContent"] : "space-evenly" }), ["alignItems"] : "center", ["textTransform"] : "uppercase", ["height"] : "6rem", ["lineHeight"] : "3.125rem", ["borderBottom"] : "0.125rem dashed #fff" }),direction:"row",gap:"3"},jsx(RadixThemesLink,{asChild:true,css:({ ["&:hover"] : ({ ["cursor"] : "pointer", ["boxShadow"] : "0 0 10px #060443, 0 0 20px #060443, 0 0 30px rgba(83, 23, 87, 0.5)", ["transform"] : "translateY(-2px)", ["transition"] : "all 0.3s ease-in-out" }) })},jsx(ReactRouterLink,{to:"/"},jsx("img",{alt:"Logotipo de Data Riders",css:({ ["@media screen and (min-width: 0)"] : ({ ["width"] : "80px" }), ["@media screen and (min-width: 30em)"] : ({ ["width"] : "100px" }), ["@media screen and (min-width: 48em)"] : ({ ["width"] : "100px" }), ["height"] : "auto" }),src:"/logo-data-riders.png"},))),jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["@media screen and (min-width: 0)"] : ({ ["gap"] : "1rem" }), ["@media screen and (min-width: 30em)"] : ({ ["gap"] : "3rem" }) })},jsx(RadixThemesLink,{asChild:true,css:({ ["position"] : "relative", ["letterSpacing"] : "0.125rem", ["textDecoration"] : "none", ["color"] : "white", ["@media screen and (min-width: 0)"] : ({ ["display"] : "none" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "flex" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "flex" }), ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{target:(false ? "_blank" : ""),to:"https://datariders.io/"},jsx(RadixThemesButton,{css:({ ["background"] : "none", ["&:hover"] : ({ ["border"] : "0.125rem solid #fff", ["backgroundColor"] : "#31175e", ["boxShadow"] : "0 0 10px #060443, 0 0 20px #060443, 0 0 30px rgba(83, 23, 87, 0.5)", ["transform"] : "translateY(-2px)", ["transition"] : "all 0.3s ease-in-out", ["cursor"] : "pointer" }) })},jsx(RadixThemesText,{as:"p"},"SITIO OFICIAL")))),jsx(RadixThemesLink,{asChild:true,css:({ ["position"] : "relative", ["letterSpacing"] : "0.125rem", ["textDecoration"] : "none", ["color"] : "white", ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })},jsx(ReactRouterLink,{target:(false ? "_blank" : ""),to:"/contacto"},jsx(RadixThemesButton,{css:({ ["background"] : "none", ["&:hover"] : ({ ["border"] : "0.125rem solid #fff", ["backgroundColor"] : "#31175e", ["boxShadow"] : "0 0 10px #060443, 0 0 20px #060443, 0 0 30px rgba(83, 23, 87, 0.5)", ["transform"] : "translateY(-2px)", ["transition"] : "all 0.3s ease-in-out", ["cursor"] : "pointer" }) })},jsx(RadixThemesText,{as:"p"},"CONTACTO")))))),jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["maxWidth"] : "900px", ["width"] : "100%", ["marginBottom"] : "20px" }),direction:"column",gap:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["marginBottom"] : "5px" }),direction:"column",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["@media screen and (min-width: 0)"] : ({ ["fontSize"] : "2em" }), ["@media screen and (min-width: 30em)"] : ({ ["fontSize"] : "2.5em" }), ["fontStyle"] : "italic", ["marginBottom"] : "0.5em", ["fontWeight"] : "bold", ["fontFamily"] : "Courier New, Courier, monospace", ["--default-font-family"] : "Courier New, Courier, monospace", ["textAlign"] : "center", ["width"] : "100%" })},"\u00a1Expandi tu negocio con nosotros!"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "1.5em", ["fontFamily"] : "Poppins-Light", ["--default-font-family"] : "Poppins-Light", ["fontWeight"] : "400", ["@media screen and (min-width: 0)"] : ({ ["paddingInlineStart"] : "20px", ["paddingInlineEnd"] : "20px" }), ["@media screen and (min-width: 30em)"] : ({ ["paddingInlineStart"] : "30px", ["paddingInlineEnd"] : "30px" }) })},"Decisiones inteligentes que transforman tu negocio. Tom\u00e1 decisiones basadas en datos y elev\u00e1 tu empresa al siguiente nivel."),jsx(RadixThemesFlex,{css:({ ["justifyContent"] : "center", ["gap"] : "1em", ["width"] : "100%", ["@media screen and (min-width: 0)"] : ({ ["display"] : "grid", ["alignItems"] : "center" }), ["@media screen and (min-width: 30em)"] : ({ ["display"] : "flex", ["alignItems"] : "normal" }), ["@media screen and (min-width: 48em)"] : ({ ["display"] : "flex" }), ["grid_template_columns"] : ({ ["base"] : "1fr" }) })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["fontSize"] : "1em", ["fontFamily"] : "Courier New, Courier, monospace", ["--default-font-family"] : "Courier New, Courier, monospace", ["@media screen and (min-width: 0)"] : ({ ["marginInlineStart"] : "0", ["marginInlineEnd"] : "0", ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["marginInlineStart"] : "15px", ["marginInlineEnd"] : "15px", ["width"] : "auto" }) }),direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#7c849c", ["fontWeight"] : "bold" })},"15+"),"a\u00f1os de experiencia"),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["fontSize"] : "1em", ["fontFamily"] : "Courier New, Courier, monospace", ["--default-font-family"] : "Courier New, Courier, monospace", ["@media screen and (min-width: 0)"] : ({ ["marginInlineStart"] : "0", ["marginInlineEnd"] : "0", ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["marginInlineStart"] : "15px", ["marginInlineEnd"] : "15px", ["width"] : "auto" }) }),direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#7c849c", ["fontWeight"] : "bold" })},"...+"),"cantidad de proyectos"),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["fontSize"] : "1em", ["fontFamily"] : "Courier New, Courier, monospace", ["--default-font-family"] : "Courier New, Courier, monospace", ["@media screen and (min-width: 0)"] : ({ ["marginInlineStart"] : "0", ["marginInlineEnd"] : "0", ["width"] : "100%" }), ["@media screen and (min-width: 30em)"] : ({ ["marginInlineStart"] : "15px", ["marginInlineEnd"] : "15px", ["width"] : "auto" }) }),direction:"row",gap:"3"},jsx(RadixThemesText,{as:"p",css:({ ["color"] : "#7c849c", ["fontWeight"] : "bold" })},"...+"),"clientes satisfechos"))),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["@media screen and (min-width: 0)"] : ({ ["paddingInlineStart"] : "1em", ["paddingInlineEnd"] : "1em" }), ["@media screen and (min-width: 30em)"] : ({ ["paddingInlineStart"] : "2em", ["paddingInlineEnd"] : "2em" }), ["@media screen and (min-width: 48em)"] : ({ ["paddingInlineStart"] : "4em", ["paddingInlineEnd"] : "4em" }) }),direction:"column",gap:"5"},jsx(Root_285a8a2bf0211d711adc4e533989e89a,{},),jsx(RadixThemesSeparator,{size:"4"},),jsx(RadixThemesHeading,{size:"5"},"Datos Recibidos (Debug)"),jsx(Text_2071de36054a691f8c6c5caebfeec8f6,{},)))),jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%", ["borderTop"] : "0.125rem dashed #31175e", ["textAlign"] : "center" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["margin"] : "1em" }),direction:"row",gap:"3"},jsx("img",{css:({ ["width"] : "25px", ["height"] : "25px" }),src:"/logotipo.png"},),jsx(RadixThemesText,{as:"p"},"\u00a9 2010-2025 DATA RIDERS - Todos los Derechos Reservados.")))),jsx("title",{},"DEMO | Contacto"),jsx("meta",{content:"Landing page para mostrar las distintas DEMO publicadas en charlas o reuniones",name:"description"},),jsx("meta",{content:"favicon.ico",property:"og:image"},),jsx("meta",{content:"website",name:"og:type"},),jsx("meta",{content:"DEMO | Data Riders",name:"og:title"},),jsx("meta",{content:"Landing page para mostrar las distintas DEMO publicadas en charlas o reuniones",name:"og:description"},))
  )
}