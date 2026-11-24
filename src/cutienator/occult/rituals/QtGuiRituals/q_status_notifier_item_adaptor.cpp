//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstatusnotifieritemadaptor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(systemtrayicon)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstatusnotifieritemadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbustraytypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qstatusnotifieritemadaptor_p.h"
#ifndef QT_NO_SYSTEMTRAYICON
#include <QtCore/QLoggingCategory>
#include <QtCore/QCoreApplication>
#include "qdbustrayicon_p.h"
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 40, as _ZNK26QStatusNotifierItemAdaptor17attentionIconNameEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::attentionIconName() const
{
    return m_trayIcon->attentionIconName();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 50, as _ZNK26QStatusNotifierItemAdaptor18attentionMovieNameEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::attentionMovieName() const
{
    return QString();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 55, as _ZNK26QStatusNotifierItemAdaptor8categoryEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::category() const
{
    return m_trayIcon->category();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 60, as _ZNK26QStatusNotifierItemAdaptor8iconNameEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::iconName() const
{
    return m_trayIcon->iconName();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 70, as _ZNK26QStatusNotifierItemAdaptor2idEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::id() const
{
    // from the API docs: "a name that should be unique for this application and
    // consistent between sessions, such as the application name itself"
    return QCoreApplication::applicationName();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 77, as _ZNK26QStatusNotifierItemAdaptor10itemIsMenuEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline bool QStatusNotifierItemAdaptor::itemIsMenu() const
{
    // From KDE docs: if this is true, the item only supports the context menu,
    // so the visualization should prefer sending ContextMenu() instead of Activate().
    // But QSystemTrayIcon doesn't have such a setting: it will emit activated()
    // and the application is free to use it or ignore it; we don't know whether it will.
    return false;
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 86, as _ZNK26QStatusNotifierItemAdaptor4menuEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QDBusObjectPath QStatusNotifierItemAdaptor::menu() const
{
    return QDBusObjectPath(m_trayIcon->menu() ? "/MenuBar" : "/NO_DBUSMENU");
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 91, as _ZNK26QStatusNotifierItemAdaptor15overlayIconNameEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::overlayIconName() const
{
    return QString();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 96, as _ZNK26QStatusNotifierItemAdaptor17overlayIconPixmapEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QXdgDBusImageVector QStatusNotifierItemAdaptor::overlayIconPixmap() const
{
    QXdgDBusImageVector ret; // empty vector
    return ret;
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 102, as _ZNK26QStatusNotifierItemAdaptor6statusEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::status() const
{
    return m_trayIcon->status();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 107, as _ZNK26QStatusNotifierItemAdaptor5titleEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QString QStatusNotifierItemAdaptor::title() const
{
    // Shown e.g. when the icon is hidden, in the popup showing all hidden items.
    // Since QSystemTrayIcon doesn't have this property, the application name
    // is the best information we have available.
    return QCoreApplication::applicationName();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qstatusnotifieritemadaptor.cpp, line 115, as _ZNK26QStatusNotifierItemAdaptor7toolTipEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QXdgDBusToolTipStruct QStatusNotifierItemAdaptor::toolTip() const
{
    QXdgDBusToolTipStruct ret;
    if (m_trayIcon->isRequestingAttention()) {
        ret.title = m_trayIcon->attentionTitle();
        ret.subTitle = m_trayIcon->attentionMessage();
        ret.icon = m_trayIcon->attentionIconName();
    } else {
        ret.title = m_trayIcon->tooltip();
    }
    return ret;
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
//  -----------------------------------------------------------------------

//  A QStatusNotifierItemAdaptor that Python can take functions over in. Every QStatusNotifierItemAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStatusNotifierItemAdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStatusNotifierItemAdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusNotifierItemAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusNotifierItemAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusNotifierItemAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusNotifierItemAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStatusNotifierItemAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStatusNotifierItemAdaptor : public QStatusNotifierItemAdaptor {
public:
  using QStatusNotifierItemAdaptor::QStatusNotifierItemAdaptor;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall0 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall1 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall2 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall3 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall4 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall5 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQStatusNotifierItemAdaptorCall6 call = reinterpret_cast<CuteQStatusNotifierItemAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStatusNotifierItemAdaptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QStatusNotifierItemAdaptor10metaObjectEv(
    const QStatusNotifierItemAdaptor *self) {
  return self->metaObject();
}

//  QStatusNotifierItemAdaptor::~QStatusNotifierItemAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStatusNotifierItemAdaptorD1Ev(
    QStatusNotifierItemAdaptor *self) {
  delete self;
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::attentionIconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor17attentionIconNameEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->attentionIconName());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::attentionMovieName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor18attentionMovieNameEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->attentionMovieName());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::category() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor8categoryEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->category());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::iconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor8iconNameEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->iconName());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor2idEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->id());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  bool QStatusNotifierItemAdaptor::itemIsMenu() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QStatusNotifierItemAdaptor10itemIsMenuEv(
    const QStatusNotifierItemAdaptor *self) {
  return self->itemIsMenu();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QDBusObjectPath QStatusNotifierItemAdaptor::menu() const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK26QStatusNotifierItemAdaptor4menuEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QDBusObjectPath(self->menu());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::overlayIconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor15overlayIconNameEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->overlayIconName());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QXdgDBusImageVector QStatusNotifierItemAdaptor::overlayIconPixmap() const
extern "C" Q_DECL_EXPORT
QList<QXdgDBusImageStruct> *ritual_ZNK26QStatusNotifierItemAdaptor17overlayIconPixmapEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QList<QXdgDBusImageStruct>(self->overlayIconPixmap());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::status() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor6statusEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->status());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QStatusNotifierItemAdaptor::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QStatusNotifierItemAdaptor5titleEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QString(self->title());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QXdgDBusToolTipStruct QStatusNotifierItemAdaptor::toolTip() const
extern "C" Q_DECL_EXPORT
QXdgDBusToolTipStruct *ritual_ZNK26QStatusNotifierItemAdaptor7toolTipEv(
    const QStatusNotifierItemAdaptor *self) {
  return new QXdgDBusToolTipStruct(self->toolTip());
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  a Python function taken by a CuteQStatusNotifierItemAdaptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStatusNotifierItemAdaptor(
    QStatusNotifierItemAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStatusNotifierItemAdaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(systemtrayicon)
