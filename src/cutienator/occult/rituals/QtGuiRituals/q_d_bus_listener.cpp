//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbuslistener_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbuslistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <optional>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qdbuslistener_p.h>
#include <QtGui/private/qdbussettings_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformservices.h>
#include <qdbusconnection.h>
#include <QtCore/qfile.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/platform/unix/qdbuslistener.cpp, line 231, as _ZNK13QDBusListener10findSignalERK7QStringS2_
inline std::optional<QDBusListener::ChangeSignal>
    QDBusListener::findSignal(const QString &location, const QString &key) const
{
    const DBusKey dkey(location, key);
    std::optional<QDBusListener::ChangeSignal> ret;
    const auto it = m_signalMap.find(dkey);
    if (it != m_signalMap.cend())
        ret.emplace(it.value());

    return ret;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QDBusListener::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QDBusListener10metaObjectEv(
    const QDBusListener *self) {
  return self->metaObject();
}

//  void *QDBusListener::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QDBusListener11qt_metacastEPKc(
    QDBusListener *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusListener::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QDBusListener11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusListener *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QDBusListener::onSettingChanged(const QString &location, const
//      QString &key, const QDBusVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusListener16onSettingChangedERK7QStringS2_RK12QDBusVariant(
    QDBusListener *self,
    const QString *location,
    const QString *key,
    const QDBusVariant *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusListener")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onSettingChanged(const QString &,const QString &,const QDBusVariant &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onSettingChanged(const QString &,const QString &,const QDBusVariant &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(location)),
      const_cast<void *>(static_cast<const void *>(key)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusListener::settingChanged(QDBusListener::Provider provider,
//      QDBusListener::Setting setting, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusListener14settingChangedENS_8ProviderENS_7SettingERK8QVariant(
    QDBusListener *self,
    QDBusListener::Provider provider,
    QDBusListener::Setting setting,
    const QVariant *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusListener")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "settingChanged(QDBusListener::Provider,QDBusListener::Setting,const QVariant &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "settingChanged(QDBusListener::Provider,QDBusListener::Setting,const QVariant &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&provider)),
      const_cast<void *>(static_cast<const void *>(&setting)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  std::optional<ChangeSignal> QDBusListener::findSignal(const QString
//      &location, const QString &key) const
extern "C" Q_DECL_EXPORT
std::optional<QDBusListener::ChangeSignal> *ritual_ZNK13QDBusListener10findSignalERK7QStringS2_(
    const QDBusListener *self,
    const QString *location,
    const QString *key) {
  return new std::optional<QDBusListener::ChangeSignal>(
      self->findSignal(
          *location,
          *key));
}

//  a std::optional<QDBusListener::ChangeSignal> a ritual of QDBusListener
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusListener__std_optional_QDBusListener_ChangeSignal(
    std::optional<QDBusListener::ChangeSignal> *self) {
  delete self;
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
