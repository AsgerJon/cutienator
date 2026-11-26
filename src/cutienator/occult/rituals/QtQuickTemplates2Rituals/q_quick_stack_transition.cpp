//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickstacktransition_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstacktransition_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickstacktransition_p_p.h>
#include <QtQuickTemplates2/private/qquickstackelement_p_p.h>
#include <QtQuickTemplates2/private/qquickstackview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickstacktransition.cpp, line 11, as local:qquickstacktransition.cpp:exitTransition
static QQuickStackTransition exitTransition(QQuickStackView::Operation operation, QQuickStackElement *element, QQuickStackView *view)
{
    QQuickStackTransition st;
    st.status = QQuickStackView::Deactivating;
    st.element = element;

    const QQuickItemViewTransitioner *transitioner = QQuickStackViewPrivate::get(view)->transitioner;

    switch (operation) {
    case QQuickStackView::PushTransition:
        st.type = QQuickItemViewTransitioner::AddTransition;
        if (transitioner)
            st.transition = transitioner->addDisplacedTransition;
        break;
    case QQuickStackView::ReplaceTransition:
        st.type = QQuickItemViewTransitioner::MoveTransition;
        if (transitioner)
            st.transition = transitioner->moveDisplacedTransition;
        break;
    case QQuickStackView::PopTransition:
        st.target = true;
        st.type = QQuickItemViewTransitioner::RemoveTransition;
        st.viewBounds = view->boundingRect();
        if (transitioner)
            st.transition = transitioner->removeTransition;
        break;
    default:
        Q_UNREACHABLE();
        break;
    }

    return st;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstacktransition.cpp, line 81, as local:qquickstacktransition.cpp:operationTransition
static QQuickStackView::Operation operationTransition(QQuickStackView::Operation operation, QQuickStackView::Operation transition)
{
    if (operation == QQuickStackView::Immediate || operation == QQuickStackView::Transition)
        return transition;
    return operation;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstacktransition.cpp, line 88, as _ZN21QQuickStackTransition7popExitEN15QQuickStackView9OperationEP18QQuickStackElementPS0_
inline QQuickStackTransition QQuickStackTransition::popExit(QQuickStackView::Operation operation, QQuickStackElement *element, QQuickStackView *view)
{
    return exitTransition(operationTransition(operation, QQuickStackView::PopTransition), element, view);
}
//  -----------------------------------------------------------------------

//  QQuickStackTransition
//      QQuickStackTransition::popExit(QQuickStackView::Operation operation,
//      QQuickStackElement *element, QQuickStackView *view)
extern "C" Q_DECL_EXPORT
QQuickStackTransition *ritual_ZN21QQuickStackTransition7popExitEN15QQuickStackView9OperationEP18QQuickStackElementPS0_(
    QQuickStackView::Operation operation,
    QQuickStackElement *element,
    QQuickStackView *view) {
  return new QQuickStackTransition(
      QQuickStackTransition::popExit(
          operation,
          element,
          view));
}

//  QQuickStackTransition::~QQuickStackTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickStackTransitionD1Ev(QQuickStackTransition *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_viewtransitions)
