//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformicon_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 9, as _ZNK22QQuickLabsPlatformIcon6sourceEv
inline QUrl QQuickLabsPlatformIcon::source() const
{
    return m_source;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 14, as _ZN22QQuickLabsPlatformIcon9setSourceERK4QUrl
inline void QQuickLabsPlatformIcon::setSource(const QUrl& source)
{
    m_source = source;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 19, as _ZNK22QQuickLabsPlatformIcon4nameEv
inline QString QQuickLabsPlatformIcon::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 24, as _ZN22QQuickLabsPlatformIcon7setNameERK7QString
inline void QQuickLabsPlatformIcon::setName(const QString& name)
{
    m_name = name;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 29, as _ZNK22QQuickLabsPlatformIcon6isMaskEv
inline bool QQuickLabsPlatformIcon::isMask() const
{
    return m_mask;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 34, as _ZN22QQuickLabsPlatformIcon7setMaskEb
inline void QQuickLabsPlatformIcon::setMask(bool mask)
{
    m_mask = mask;
}
//  -----------------------------------------------------------------------

//  void QQuickLabsPlatformIcon::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformIcon22qt_qmlMarker_anonymousEv(
    QQuickLabsPlatformIcon *self) {
  self->qt_qmlMarker_anonymous();
}

//  QUrl QQuickLabsPlatformIcon::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QQuickLabsPlatformIcon6sourceEv(
    const QQuickLabsPlatformIcon *self) {
  return new QUrl(self->source());
}

//  void QQuickLabsPlatformIcon::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformIcon9setSourceERK4QUrl(
    QQuickLabsPlatformIcon *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QString QQuickLabsPlatformIcon::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickLabsPlatformIcon4nameEv(
    const QQuickLabsPlatformIcon *self) {
  return new QString(self->name());
}

//  void QQuickLabsPlatformIcon::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformIcon7setNameERK7QString(
    QQuickLabsPlatformIcon *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QQuickLabsPlatformIcon::isMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickLabsPlatformIcon6isMaskEv(
    const QQuickLabsPlatformIcon *self) {
  return self->isMask();
}

//  void QQuickLabsPlatformIcon::setMask(bool mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformIcon7setMaskEb(
    QQuickLabsPlatformIcon *self,
    bool mask) {
  self->setMask(mask);
}

//  QQuickLabsPlatformIcon::~QQuickLabsPlatformIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformIconD1Ev(QQuickLabsPlatformIcon *self) {
  delete self;
}
