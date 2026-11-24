//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicklabsplatformfiledialog_p.h"
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/qlist.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 552, as _ZNK32QQuickLabsPlatformFileNameFilter5indexEv
#if QT_DEPRECATED_SINCE(6, 9)
inline int QQuickLabsPlatformFileNameFilter::index() const
{
    return m_index;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 566, as _ZNK32QQuickLabsPlatformFileNameFilter4nameEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileNameFilter::name() const
{
    return m_name;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 571, as _ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::extensions() const
{
    return m_extensions;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 631, as _ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
{
    return m_options ? m_options->nameFilters() : QStringList();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 636, as _ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
{
    return m_options ? m_options->nameFilters().value(index) : QString();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickLabsPlatformFileNameFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickLabsPlatformFileNameFilter10metaObjectEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return self->metaObject();
}

//  void QQuickLabsPlatformFileNameFilter::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformFileNameFilter22qt_qmlMarker_anonymousEv(
    QQuickLabsPlatformFileNameFilter *self) {
  self->qt_qmlMarker_anonymous();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  int QQuickLabsPlatformFileNameFilter::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QQuickLabsPlatformFileNameFilter5indexEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return self->index();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformFileNameFilter4nameEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QString(self->name());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileNameFilter::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QList<QString>(self->extensions());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv(
    const QQuickLabsPlatformFileNameFilter *self) {
  return new QList<QString>(self->nameFilters());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi(
    const QQuickLabsPlatformFileNameFilter *self,
    int index) {
  return new QString(self->nameFilter(index));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)
