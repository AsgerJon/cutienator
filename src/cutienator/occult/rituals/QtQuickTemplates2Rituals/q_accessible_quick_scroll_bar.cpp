//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qaccessiblequickscrollbar_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/QList>
#include <QtGui/QAccessible>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qaccessiblequickcontrol_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtQuickTemplates2/private/qaccessiblequickscrollbar_p.h>
#include <QtQuickTemplates2/private/qquickscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 10, as _ZN23QAccessibleQuickControlC2EP13QQuickControl
inline QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl *control)
    : QAccessibleQuickItem(control)
{
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 15, as _ZNK25QAccessibleQuickScrollBar13attributeKeysEv
inline QList<QAccessible::Attribute> QAccessibleQuickScrollBar::attributeKeys() const
{
    QList<QAccessible::Attribute> keys = QAccessibleQuickControl::attributeKeys();
    keys.append(QAccessible::Attribute::Orientation);

    return keys;
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 23, as _ZNK25QAccessibleQuickScrollBar14attributeValueEN11QAccessible9AttributeE
inline QVariant QAccessibleQuickScrollBar::attributeValue(QAccessible::Attribute key) const
{
    if (key == QAccessible::Attribute::Orientation)
        return QVariant::fromValue(scrollBar()->orientation());

    return QAccessibleQuickControl::attributeValue(key);
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 31, as _ZNK25QAccessibleQuickScrollBar12currentValueEv
inline QVariant QAccessibleQuickScrollBar::currentValue() const
{
    return normalizeValue(scrollBar()->position());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 36, as _ZN25QAccessibleQuickScrollBar15setCurrentValueERK8QVariant
inline void QAccessibleQuickScrollBar::setCurrentValue(const QVariant &value)
{
    scrollBar()->setPosition(denormalizeValue(value.toReal()));
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 41, as _ZNK25QAccessibleQuickScrollBar12maximumValueEv
inline QVariant QAccessibleQuickScrollBar::maximumValue() const
{
    return normalizeValue(1.0 - scrollBar()->size());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 46, as _ZNK25QAccessibleQuickScrollBar12minimumValueEv
inline QVariant QAccessibleQuickScrollBar::minimumValue() const
{
    return normalizeValue(0.0);
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 51, as _ZNK25QAccessibleQuickScrollBar15minimumStepSizeEv
inline QVariant QAccessibleQuickScrollBar::minimumStepSize() const
{
    return normalizeValue(scrollBar()->stepSize());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 15, as _ZNK23QAccessibleQuickControl13attributeKeysEv
inline QList<QAccessible::Attribute> QAccessibleQuickControl::attributeKeys() const
{
    auto keys = QAccessibleQuickItem::attributeKeys();
    if (!keys.contains(QAccessible::Attribute::Locale))
        keys << QAccessible::Attribute::Locale;

    return keys;
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 24, as _ZNK23QAccessibleQuickControl14attributeValueEN11QAccessible9AttributeE
inline QVariant QAccessibleQuickControl::attributeValue(QAccessible::Attribute key) const
{
    if (key == QAccessible::Attribute::Locale)
        return QVariant::fromValue(control()->locale());

    return QAccessibleQuickItem::attributeValue(key);
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 32, as _ZNK23QAccessibleQuickControl7controlEv
inline QQuickControl *QAccessibleQuickControl::control() const
{
    return static_cast<QQuickControl *>(object());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 56, as _ZNK25QAccessibleQuickScrollBar9scrollBarEv
inline QQuickScrollBar *QAccessibleQuickScrollBar::scrollBar() const
{
    return static_cast<QQuickScrollBar *>(object());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 61, as _ZNK25QAccessibleQuickScrollBar20maximumPositionValueEv
inline qreal QAccessibleQuickScrollBar::maximumPositionValue() const
{
    return 1.0 - scrollBar()->size();
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 66, as _ZNK25QAccessibleQuickScrollBar14normalizeValueEd
inline qreal QAccessibleQuickScrollBar::normalizeValue(qreal value) const
{
    const qreal maxPositionValue = maximumPositionValue();
    if (maxPositionValue > 0.0)
        return value / maxPositionValue * 100.0;
    return 0;
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickscrollbar.cpp, line 74, as _ZNK25QAccessibleQuickScrollBar16denormalizeValueEd
inline qreal QAccessibleQuickScrollBar::denormalizeValue(qreal value) const
{
    return value / 100.0 * maximumPositionValue();
}
//  -----------------------------------------------------------------------

//  QList<QAccessible::Attribute> QAccessibleQuickScrollBar::attributeKeys()
//      const
extern "C" Q_DECL_EXPORT
QList<QAccessible::Attribute> *ritual_ZNK25QAccessibleQuickScrollBar13attributeKeysEv(
    const QAccessibleQuickScrollBar *self) {
  return new QList<QAccessible::Attribute>(self->attributeKeys());
}

//  QVariant QAccessibleQuickScrollBar::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleQuickScrollBar14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickScrollBar *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QVariant QAccessibleQuickScrollBar::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleQuickScrollBar12currentValueEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->currentValue());
}

//  void QAccessibleQuickScrollBar::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleQuickScrollBar15setCurrentValueERK8QVariant(
    QAccessibleQuickScrollBar *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QAccessibleQuickScrollBar::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleQuickScrollBar12maximumValueEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleQuickScrollBar::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleQuickScrollBar12minimumValueEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleQuickScrollBar::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleQuickScrollBar15minimumStepSizeEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->minimumStepSize());
}

//  QQuickScrollBar *QAccessibleQuickScrollBar::scrollBar() const
extern "C" Q_DECL_EXPORT
QQuickScrollBar *ritual_ZNK25QAccessibleQuickScrollBar9scrollBarEv(
    const QAccessibleQuickScrollBar *self) {
  return self->scrollBar();
}

//  qreal QAccessibleQuickScrollBar::maximumPositionValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QAccessibleQuickScrollBar20maximumPositionValueEv(
    const QAccessibleQuickScrollBar *self) {
  return self->maximumPositionValue();
}

//  qreal QAccessibleQuickScrollBar::normalizeValue(qreal value) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QAccessibleQuickScrollBar14normalizeValueEd(
    const QAccessibleQuickScrollBar *self,
    qreal value) {
  return self->normalizeValue(value);
}

//  qreal QAccessibleQuickScrollBar::denormalizeValue(qreal value) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QAccessibleQuickScrollBar16denormalizeValueEd(
    const QAccessibleQuickScrollBar *self,
    qreal value) {
  return self->denormalizeValue(value);
}

//  QVariant QAccessibleQuickScrollBar::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleQuickScrollBar14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickScrollBar *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleQuickScrollBar::attributeValue(key));
}

//  QVariant QAccessibleQuickScrollBar::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleQuickScrollBar12currentValueEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->QAccessibleQuickScrollBar::currentValue());
}

//  void QAccessibleQuickScrollBar::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleQuickScrollBar15setCurrentValueERK8QVariant(
    QAccessibleQuickScrollBar *self,
    const QVariant *value) {
  self->QAccessibleQuickScrollBar::setCurrentValue(*value);
}

//  QVariant QAccessibleQuickScrollBar::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleQuickScrollBar12maximumValueEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->QAccessibleQuickScrollBar::maximumValue());
}

//  QVariant QAccessibleQuickScrollBar::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleQuickScrollBar12minimumValueEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->QAccessibleQuickScrollBar::minimumValue());
}

//  QVariant QAccessibleQuickScrollBar::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleQuickScrollBar15minimumStepSizeEv(
    const QAccessibleQuickScrollBar *self) {
  return new QVariant(self->QAccessibleQuickScrollBar::minimumStepSize());
}

//  a QList<QAccessible::Attribute> a ritual of QAccessibleQuickScrollBar
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAccessibleQuickScrollBar__QList_QAccessible_Attribute(
    QList<QAccessible::Attribute> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
