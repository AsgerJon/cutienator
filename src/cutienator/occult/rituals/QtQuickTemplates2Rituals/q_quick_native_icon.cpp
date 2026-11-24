//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativeicon_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativeicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicknativeicon_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquicknativeicon.cpp, line 9, as _ZNK16QQuickNativeIcon6sourceEv
inline QUrl QQuickNativeIcon::source() const
{
    return m_source;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeicon.cpp, line 14, as _ZN16QQuickNativeIcon9setSourceERK4QUrl
inline void QQuickNativeIcon::setSource(const QUrl& source)
{
    m_source = source;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeicon.cpp, line 19, as _ZNK16QQuickNativeIcon4nameEv
inline QString QQuickNativeIcon::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeicon.cpp, line 24, as _ZN16QQuickNativeIcon7setNameERK7QString
inline void QQuickNativeIcon::setName(const QString& name)
{
    m_name = name;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeicon.cpp, line 29, as _ZNK16QQuickNativeIcon6isMaskEv
inline bool QQuickNativeIcon::isMask() const
{
    return m_mask;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeicon.cpp, line 34, as _ZN16QQuickNativeIcon7setMaskEb
inline void QQuickNativeIcon::setMask(bool mask)
{
    m_mask = mask;
}
//  -----------------------------------------------------------------------

//  void QQuickNativeIcon::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickNativeIcon22qt_qmlMarker_anonymousEv(
    QQuickNativeIcon *self) {
  self->qt_qmlMarker_anonymous();
}

//  QUrl QQuickNativeIcon::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQuickNativeIcon6sourceEv(const QQuickNativeIcon *self) {
  return new QUrl(self->source());
}

//  void QQuickNativeIcon::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickNativeIcon9setSourceERK4QUrl(
    QQuickNativeIcon *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QString QQuickNativeIcon::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickNativeIcon4nameEv(const QQuickNativeIcon *self) {
  return new QString(self->name());
}

//  void QQuickNativeIcon::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickNativeIcon7setNameERK7QString(
    QQuickNativeIcon *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QQuickNativeIcon::isMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickNativeIcon6isMaskEv(const QQuickNativeIcon *self) {
  return self->isMask();
}

//  void QQuickNativeIcon::setMask(bool mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickNativeIcon7setMaskEb(
    QQuickNativeIcon *self,
    bool mask) {
  self->setMask(mask);
}

//  QQuickNativeIcon::~QQuickNativeIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickNativeIconD1Ev(QQuickNativeIcon *self) {
  delete self;
}
