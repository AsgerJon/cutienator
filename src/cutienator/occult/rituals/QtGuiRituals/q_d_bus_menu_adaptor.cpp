//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenuadaptor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenuadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtCore/QMetaObject>
#include <QtCore/QByteArray>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QVariant>
#include <QtCore/QLocale>
#include <QtGui/private/qdbusmenuadaptor_p.h>
#include <QtGui/private/qdbusplatformmenu_p.h>
#include <QtGui/private/qdbusmenutypes_p.h>
#include <QDBusConnection>
#include <QDBusMetaType>
#include <QtGui/QImage>
#include <QtGui/QIcon>
#include <QtGui/QImage>
#include <QtGui/QPixmap>
#include <QtCore/QDebug>
#include <QtCore/QtEndian>
#include <QtCore/QBuffer>
#if QT_CONFIG(shortcut)
#  include <QtGui/private/qkeysequence_p.h>
#endif
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/private/qdbusplatformmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 13, as _Z7qLcMenuv
inline const QLoggingCategory &qLcMenu()
{
    static const QLoggingCategory category("qt.qpa.menu");
    return category;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuadaptor.cpp, line 82, as _ZN16QDBusMenuAdaptor5EventEiRK7QStringRK12QDBusVariantj
inline void QDBusMenuAdaptor::Event(int id, const QString &eventId, const QDBusVariant &data, uint timestamp)
{
    Q_UNUSED(data);
    Q_UNUSED(timestamp);
    QDBusPlatformMenuItem *item = QDBusPlatformMenuItem::byId(id);
    qCDebug(qLcMenu) << id << (item ? item->text() : ""_L1) << eventId;
    if (item && eventId == "clicked"_L1)
        item->trigger();
    if (item && eventId == "hovered"_L1)
        emit item->hovered();
    if (eventId == "closed"_L1) {
        // There is no explicit AboutToHide method, so map closed event to aboutToHide method
        const QDBusPlatformMenu *menu = nullptr;
        if (item)
            menu = static_cast<const QDBusPlatformMenu *>(item->menu());
        else if (id == 0)
            menu = m_topLevelMenu;
        if (menu)
            emit const_cast<QDBusPlatformMenu *>(menu)->aboutToHide();
    }
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 192, as _ZN13QDBusMenuItem5itemsERK5QListIiERKS0_I7QStringE
inline QDBusMenuItemList QDBusMenuItem::items(const QList<int> &ids, const QStringList &propertyNames)
{
    Q_UNUSED(propertyNames);
    QDBusMenuItemList ret;
    const QList<const QDBusPlatformMenuItem *> items = QDBusPlatformMenuItem::byIds(ids);
    ret.reserve(items.size());
    for (const QDBusPlatformMenuItem *item : items)
        ret << QDBusMenuItem(item);
    return ret;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 68, as _ZN19QDBusMenuLayoutItem8populateEiiRK5QListI7QStringEPK17QDBusPlatformMenu
inline uint QDBusMenuLayoutItem::populate(int id, int depth, const QStringList &propertyNames, const QDBusPlatformMenu *topLevelMenu)
{
    qCDebug(qLcMenu) << id << "depth" << depth << propertyNames;
    m_id = id;
    if (id == 0) {
        m_properties.insert("children-display"_L1, "submenu"_L1);
        if (topLevelMenu)
            populate(topLevelMenu, depth, propertyNames);
        return 1; // revision
    }

    QDBusPlatformMenuItem *item = QDBusPlatformMenuItem::byId(id);
    if (item) {
        const QDBusPlatformMenu *menu = static_cast<const QDBusPlatformMenu *>(item->menu());

        if (menu) {
            if (depth != 0)
                populate(menu, depth, propertyNames);
            return menu->revision();
        }
    }

    return 1; // revision
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuadaptor.cpp, line 40, as _ZNK16QDBusMenuAdaptor6statusEv
inline QString QDBusMenuAdaptor::status() const
{
    qCDebug(qLcMenu);
    return "normal"_L1;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuadaptor.cpp, line 46, as _ZNK16QDBusMenuAdaptor13textDirectionEv
inline QString QDBusMenuAdaptor::textDirection() const
{
    return QLocale().textDirection() == Qt::RightToLeft ? "rtl"_L1 : "ltr"_L1;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuadaptor.cpp, line 51, as _ZNK16QDBusMenuAdaptor7versionEv
inline uint QDBusMenuAdaptor::version() const
{
    return 4;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuadaptor.cpp, line 124, as _ZN16QDBusMenuAdaptor11GetPropertyEiRK7QString
inline QDBusVariant QDBusMenuAdaptor::GetProperty(int id, const QString &name)
{
    qCDebug(qLcMenu) << id << name;
    // handle method call com.canonical.dbusmenu.GetProperty
    QDBusVariant value;
    return value;
}
//  -----------------------------------------------------------------------

//  A QDBusMenuAdaptor that Python can take functions over in. Every QDBusMenuAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuAdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuAdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusMenuAdaptor : public QDBusMenuAdaptor {
public:
  using QDBusMenuAdaptor::QDBusMenuAdaptor;
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
      CuteQDBusMenuAdaptorCall0 call = reinterpret_cast<CuteQDBusMenuAdaptorCall0>(taken[0]);
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
      CuteQDBusMenuAdaptorCall1 call = reinterpret_cast<CuteQDBusMenuAdaptorCall1>(taken[1]);
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
      CuteQDBusMenuAdaptorCall2 call = reinterpret_cast<CuteQDBusMenuAdaptorCall2>(taken[2]);
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
      CuteQDBusMenuAdaptorCall3 call = reinterpret_cast<CuteQDBusMenuAdaptorCall3>(taken[3]);
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
      CuteQDBusMenuAdaptorCall4 call = reinterpret_cast<CuteQDBusMenuAdaptorCall4>(taken[4]);
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
      CuteQDBusMenuAdaptorCall5 call = reinterpret_cast<CuteQDBusMenuAdaptorCall5>(taken[5]);
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
      CuteQDBusMenuAdaptorCall6 call = reinterpret_cast<CuteQDBusMenuAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusMenuAdaptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QDBusMenuAdaptor10metaObjectEv(
    const QDBusMenuAdaptor *self) {
  return self->metaObject();
}

//  void *QDBusMenuAdaptor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QDBusMenuAdaptor11qt_metacastEPKc(
    QDBusMenuAdaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusMenuAdaptor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QDBusMenuAdaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusMenuAdaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QDBusMenuAdaptor::~QDBusMenuAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusMenuAdaptorD1Ev(QDBusMenuAdaptor *self) {
  delete self;
}

//  QString QDBusMenuAdaptor::status() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDBusMenuAdaptor6statusEv(
    const QDBusMenuAdaptor *self) {
  return new QString(self->status());
}

//  QString QDBusMenuAdaptor::textDirection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDBusMenuAdaptor13textDirectionEv(
    const QDBusMenuAdaptor *self) {
  return new QString(self->textDirection());
}

//  uint QDBusMenuAdaptor::version() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QDBusMenuAdaptor7versionEv(const QDBusMenuAdaptor *self) {
  return self->version();
}

//  void QDBusMenuAdaptor::Event(int id, const QString &eventId, const
//      QDBusVariant &data, uint timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusMenuAdaptor5EventEiRK7QStringRK12QDBusVariantj(
    QDBusMenuAdaptor *self,
    int id,
    const QString *eventId,
    const QDBusVariant *data,
    uint timestamp) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusMenuAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "Event(int,const QString &,const QDBusVariant &,uint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "Event(int,const QString &,const QDBusVariant &,uint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(eventId)),
      const_cast<void *>(static_cast<const void *>(data)),
      const_cast<void *>(static_cast<const void *>(&timestamp)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QDBusVariant QDBusMenuAdaptor::GetProperty(int id, const QString &name)
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN16QDBusMenuAdaptor11GetPropertyEiRK7QString(
    QDBusMenuAdaptor *self,
    int id,
    const QString *name) {
  return new QDBusVariant(self->GetProperty(id, *name));
}

//  void QDBusMenuAdaptor::ItemActivationRequested(int id, uint timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusMenuAdaptor23ItemActivationRequestedEij(
    QDBusMenuAdaptor *self,
    int id,
    uint timestamp) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusMenuAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ItemActivationRequested(int,uint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ItemActivationRequested(int,uint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(&timestamp)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusMenuAdaptor::ItemsPropertiesUpdated(const QDBusMenuItemList
//      &updatedProps, const QDBusMenuItemKeysList &removedProps)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusMenuAdaptor22ItemsPropertiesUpdatedERK5QListI13QDBusMenuItemERKS0_I17QDBusMenuItemKeysE(
    QDBusMenuAdaptor *self,
    const QList<QDBusMenuItem> *updatedProps,
    const QList<QDBusMenuItemKeys> *removedProps) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusMenuAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ItemsPropertiesUpdated(const QDBusMenuItemList &,const QDBusMenuItemKeysList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ItemsPropertiesUpdated(const QDBusMenuItemList &,const QDBusMenuItemKeysList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(updatedProps)),
      const_cast<void *>(static_cast<const void *>(removedProps)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusMenuAdaptor::LayoutUpdated(uint revision, int parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusMenuAdaptor13LayoutUpdatedEji(
    QDBusMenuAdaptor *self,
    uint revision,
    int parent) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusMenuAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "LayoutUpdated(uint,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "LayoutUpdated(uint,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&revision)),
      const_cast<void *>(static_cast<const void *>(&parent)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQDBusMenuAdaptor, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusMenuAdaptor(
    QDBusMenuAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusMenuAdaptor *>(self)->take(key, call);
}

//  a QList<int> a ritual of QDBusMenuAdaptor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusMenuAdaptor__QList_int(QList<int> *self) {
  delete self;
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
