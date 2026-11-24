//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qqui
//  ckmaterialplaceholdertext_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2MaterialStyleImpl/QtQuickControls2MaterialStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialplaceholdertext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickmaterialplaceholdertext_p.h"
#include <QtCore/qpropertyanimation.h>
#include <QtCore/qparallelanimationgroup.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuickTemplates2/private/qquicktheme_p.h>
#include <QtQuickTemplates2/private/qquicktextarea_p.h>
#include <QtQuickTemplates2/private/qquicktextfield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 37, as _ZNK29QQuickMaterialPlaceholderText8isFilledEv
inline bool QQuickMaterialPlaceholderText::isFilled() const
{
    return m_filled;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 42, as _ZN29QQuickMaterialPlaceholderText9setFilledEb
inline void QQuickMaterialPlaceholderText::setFilled(bool filled)
{
    if (filled == m_filled)
        return;

    m_filled = filled;
    update();
    void filledChanged();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 170, as _ZNK29QQuickMaterialPlaceholderText13largestHeightEv
inline int QQuickMaterialPlaceholderText::largestHeight() const
{
    return m_largestHeight;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 52, as _ZNK29QQuickMaterialPlaceholderText21controlHasActiveFocusEv
inline bool QQuickMaterialPlaceholderText::controlHasActiveFocus() const
{
    return m_controlHasActiveFocus;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 67, as _ZNK29QQuickMaterialPlaceholderText14controlHasTextEv
inline bool QQuickMaterialPlaceholderText::controlHasText() const
{
    return m_controlHasText;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 175, as _ZNK29QQuickMaterialPlaceholderText31controlImplicitBackgroundHeightEv
inline qreal QQuickMaterialPlaceholderText::controlImplicitBackgroundHeight() const
{
    return m_controlImplicitBackgroundHeight;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 200, as _ZNK29QQuickMaterialPlaceholderText13controlHeightEv
inline qreal QQuickMaterialPlaceholderText::controlHeight() const
{
    return m_controlHeight;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 214, as _ZNK29QQuickMaterialPlaceholderText15verticalPaddingEv
inline qreal QQuickMaterialPlaceholderText::verticalPadding() const
{
    return m_verticalPadding;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 247, as _ZN29QQuickMaterialPlaceholderText21adjustTransformOriginEv
inline void QQuickMaterialPlaceholderText::adjustTransformOrigin()
{
    switch (effectiveHAlign()) {
    case QQuickText::AlignLeft:
        Q_FALLTHROUGH();
    case QQuickText::AlignJustify:
        setTransformOrigin(QQuickItem::Left);
        break;
    case QQuickText::AlignRight:
        setTransformOrigin(QQuickItem::Right);
        break;
    case QQuickText::AlignHCenter:
        setTransformOrigin(QQuickItem::Center);
        break;
    }
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 88, as _ZNK29QQuickMaterialPlaceholderText11shouldFloatEv
inline bool QQuickMaterialPlaceholderText::shouldFloat() const
{
    const bool controlHasActiveFocusOrText = m_controlHasActiveFocus || m_controlHasText;
    return m_filled
        ? controlHasActiveFocusOrText
        : !text().isEmpty() && controlHasActiveFocusOrText;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 96, as _ZNK29QQuickMaterialPlaceholderText13shouldAnimateEv
inline bool QQuickMaterialPlaceholderText::shouldAnimate() const
{
    return m_filled
        ? !m_controlHasText
        : !m_controlHasText && !text().isEmpty();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 108, as _ZN29QQuickMaterialPlaceholderText7updateXEv
inline void QQuickMaterialPlaceholderText::updateX()
{
    setX(shouldFloat() ? floatingTargetX() : normalTargetX());
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 155, as _ZNK29QQuickMaterialPlaceholderText13normalTargetXEv
inline qreal QQuickMaterialPlaceholderText::normalTargetX() const
{
    return m_leftPadding;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 160, as _ZNK29QQuickMaterialPlaceholderText15floatingTargetXEv
inline qreal QQuickMaterialPlaceholderText::floatingTargetX() const
{
    return m_floatingLeftPadding;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialplaceholdertext.cpp, line 322, as _ZN29QQuickMaterialPlaceholderText17componentCompleteEv
inline void QQuickMaterialPlaceholderText::componentComplete()
{
    QQuickPlaceholderText::componentComplete();

    adjustTransformOrigin();

    m_largestHeight = implicitHeight();
    if (m_largestHeight > 0) {
        emit largestHeightChanged();
    } else {
        qmlWarning(this) << "Expected implicitHeight of placeholder text" << text()
            << "to be greater than 0 by component completion!";
    }

    updateFocusAnimation();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickMaterialPlaceholderText::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickMaterialPlaceholderText10metaObjectEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->metaObject();
}

//  bool QQuickMaterialPlaceholderText::isFilled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickMaterialPlaceholderText8isFilledEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->isFilled();
}

//  void QQuickMaterialPlaceholderText::setFilled(bool filled)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickMaterialPlaceholderText9setFilledEb(
    QQuickMaterialPlaceholderText *self,
    bool filled) {
  self->setFilled(filled);
}

//  int QQuickMaterialPlaceholderText::largestHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickMaterialPlaceholderText13largestHeightEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->largestHeight();
}

//  bool QQuickMaterialPlaceholderText::controlHasActiveFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickMaterialPlaceholderText21controlHasActiveFocusEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->controlHasActiveFocus();
}

//  bool QQuickMaterialPlaceholderText::controlHasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickMaterialPlaceholderText14controlHasTextEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->controlHasText();
}

//  qreal QQuickMaterialPlaceholderText::controlImplicitBackgroundHeight()
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QQuickMaterialPlaceholderText31controlImplicitBackgroundHeightEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->controlImplicitBackgroundHeight();
}

//  qreal QQuickMaterialPlaceholderText::controlHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QQuickMaterialPlaceholderText13controlHeightEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->controlHeight();
}

//  qreal QQuickMaterialPlaceholderText::verticalPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QQuickMaterialPlaceholderText15verticalPaddingEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->verticalPadding();
}

//  void QQuickMaterialPlaceholderText::adjustTransformOrigin()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickMaterialPlaceholderText21adjustTransformOriginEv(
    QQuickMaterialPlaceholderText *self) {
  self->adjustTransformOrigin();
}

//  bool QQuickMaterialPlaceholderText::shouldFloat() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickMaterialPlaceholderText11shouldFloatEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->shouldFloat();
}

//  bool QQuickMaterialPlaceholderText::shouldAnimate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickMaterialPlaceholderText13shouldAnimateEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->shouldAnimate();
}

//  void QQuickMaterialPlaceholderText::updateX()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickMaterialPlaceholderText7updateXEv(
    QQuickMaterialPlaceholderText *self) {
  self->updateX();
}

//  qreal QQuickMaterialPlaceholderText::normalTargetX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QQuickMaterialPlaceholderText13normalTargetXEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->normalTargetX();
}

//  qreal QQuickMaterialPlaceholderText::floatingTargetX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QQuickMaterialPlaceholderText15floatingTargetXEv(
    const QQuickMaterialPlaceholderText *self) {
  return self->floatingTargetX();
}

//  void QQuickMaterialPlaceholderText::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickMaterialPlaceholderText17componentCompleteEv(
    QQuickMaterialPlaceholderText *self) {
  self->componentComplete();
}
