//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickstackview_p.h>
#include <QtQuickTemplates2/private/qquickstackview_p_p.h>
#include <QtQuickTemplates2/private/qquickstackelement_p_p.h>
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuickTemplates2/private/qquickstacktransition_p_p.h>
#endif
#include <QtCore/qscopedvaluerollback.h>
#include <QtQml/qjsvalue.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickstackview.cpp, line 23, as _ZN18QQuickStackViewArgC1EP10QQuickItem
inline QQuickStackViewArg::QQuickStackViewArg(QQuickItem *item)
    : mItem(item)
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview.cpp, line 28, as _ZN18QQuickStackViewArgC1ERK4QUrl
inline QQuickStackViewArg::QQuickStackViewArg(const QUrl &url)
    : mUrl(url)
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview.cpp, line 33, as _ZN18QQuickStackViewArgC1EP13QQmlComponent
inline QQuickStackViewArg::QQuickStackViewArg(QQmlComponent *component)
    : mComponent(component)
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview.cpp, line 38, as _ZN18QQuickStackViewArgC1ERK4QMapI7QString8QVariantE
inline QQuickStackViewArg::QQuickStackViewArg(const QVariantMap &properties)
    : mProperties(properties)
{
}
//  -----------------------------------------------------------------------

//  void QQuickStackViewArg::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackViewArg22qt_qmlMarker_anonymousEv(
    QQuickStackViewArg *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickStackViewArg::QQuickStackViewArg()
extern "C" Q_DECL_EXPORT
QQuickStackViewArg *ritual_ZN18QQuickStackViewArgC1Ev() {
  return new QQuickStackViewArg();
}

//  QQuickStackViewArg::QQuickStackViewArg(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickStackViewArg *ritual_ZN18QQuickStackViewArgC1EP10QQuickItem(
    QQuickItem *item) {
  return new QQuickStackViewArg(item);
}

//  QQuickStackViewArg::QQuickStackViewArg(const QUrl &url)
extern "C" Q_DECL_EXPORT
QQuickStackViewArg *ritual_ZN18QQuickStackViewArgC1ERK4QUrl(
    const QUrl *url) {
  return new QQuickStackViewArg(*url);
}

//  QQuickStackViewArg::QQuickStackViewArg(QQmlComponent *component)
extern "C" Q_DECL_EXPORT
QQuickStackViewArg *ritual_ZN18QQuickStackViewArgC1EP13QQmlComponent(
    QQmlComponent *component) {
  return new QQuickStackViewArg(component);
}

//  QQuickStackViewArg::QQuickStackViewArg(const QVariantMap &properties)
extern "C" Q_DECL_EXPORT
QQuickStackViewArg *ritual_ZN18QQuickStackViewArgC1ERK4QMapI7QString8QVariantE(
    const QMap<QString, QVariant> *properties) {
  return new QQuickStackViewArg(*properties);
}

//  QQuickStackViewArg::~QQuickStackViewArg()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackViewArgD1Ev(QQuickStackViewArg *self) {
  delete self;
}

//  QList<QQuickStackViewArg>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickStackViewArg> *ritual_list_make_QQuickStackViewArg() {
  return new QList<QQuickStackViewArg>();
}

//  void QList<QQuickStackViewArg>::append(const QQuickStackViewArg &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickStackViewArg(
    QList<QQuickStackViewArg> *self,
    const QQuickStackViewArg *element) {
  self->append(*element);
}

//  qsizetype QList<QQuickStackViewArg>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickStackViewArg(
    const QList<QQuickStackViewArg> *self) {
  return self->size();
}

//  const QQuickStackViewArg &QList<QQuickStackViewArg>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuickStackViewArg *ritual_list_at_QQuickStackViewArg(
    const QList<QQuickStackViewArg> *self,
    long long index) {
  return new QQuickStackViewArg(self->at(index));
}

//  QList<QQuickStackViewArg>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickStackViewArg(QList<QQuickStackViewArg> *self) {
  delete self;
}
