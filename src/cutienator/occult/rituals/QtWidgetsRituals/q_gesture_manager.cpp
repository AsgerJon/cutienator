//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgesturemanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_GESTURES)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgesturemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtWidgets/private/qstandardgestures_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/private/qgesture_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicsitem.h>
#endif
#include <QtGui/private/qevent_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidgetwindow_p.h>
#include <QtWidgets/qgesture.h>
#include <QtGui/qevent.h>
#ifdef Q_OS_HARMONY
#include <QtWidgets/private/qohosgesturerecognizer_p.h>
#endif
#ifdef Q_OS_MACOS
#include <QtWidgets/private/qmacgesturerecognizer_p.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/QVarLengthArray>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/kernel/qgesturemanager.cpp, line 81, as _ZN15QGestureManagerD1Ev
#if !defined(QT_NO_GESTURES)
inline QGestureManager::~QGestureManager()
{
    qDeleteAll(m_recognizers);
    for (auto it = m_obsoleteGestures.cbegin(), end = m_obsoleteGestures.cend(); it != end; ++it) {
        qDeleteAll(it.value());
        delete it.key();
    }
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qgesturemanager.cpp, line 90, as _ZN15QGestureManager25registerGestureRecognizerEP18QGestureRecognizer
#if !defined(QT_NO_GESTURES)
inline Qt::GestureType QGestureManager::registerGestureRecognizer(QGestureRecognizer *recognizer)
{
    const QScopedPointer<QGesture> dummy(recognizer->create(nullptr));
    if (Q_UNLIKELY(!dummy)) {
        qWarning("QGestureManager::registerGestureRecognizer: "
                 "the recognizer fails to create a gesture object, skipping registration.");
        return Qt::GestureType(0);
    }
    Qt::GestureType type = dummy->gestureType();
    if (type == Qt::CustomGesture) {
        // generate a new custom gesture id
        ++m_lastCustomGestureId;
        type = Qt::GestureType(m_lastCustomGestureId);
    }
    m_recognizers.insert(type, recognizer);
    return type;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qgesturemanager.cpp, line 108, as _ZN15QGestureManager27unregisterGestureRecognizerEN2Qt11GestureTypeE
#if !defined(QT_NO_GESTURES)
inline void QGestureManager::unregisterGestureRecognizer(Qt::GestureType type)
{
    QList<QGestureRecognizer *> list = m_recognizers.values(type);
    m_recognizers.remove(type);
    for (const auto &[g, recognizer] : std::as_const(m_gestureToRecognizer).asKeyValueRange()) {
        if (list.contains(recognizer)) {
            m_deletedRecognizers.insert(g, recognizer);
        }
    }

    for (const auto &[objectGesture, gestures] : std::as_const(m_objectGestures).asKeyValueRange()) {
        if (objectGesture.gesture == type) {
            for (QGesture *g : gestures) {
                auto it = m_gestureToRecognizer.constFind(g);
                if (it != m_gestureToRecognizer.cend() && it.value()) {
                    QGestureRecognizer *recognizer = it.value();
                    m_gestureToRecognizer.erase(it);
                    m_obsoleteGestures[recognizer].insert(g);
                }
            }
        }
    }

    for (QGestureRecognizer *recognizer : std::as_const(list)) {
        const bool isObsolete = m_obsoleteGestures.contains(recognizer);
        const bool isDeleted = m_deletedRecognizers.values().contains(recognizer);

        if (!isObsolete && !isDeleted)
            delete recognizer;
    }
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qgesturemanager.cpp, line 140, as _ZN15QGestureManager21cleanupCachedGesturesEP7QObjectN2Qt11GestureTypeE
#if !defined(QT_NO_GESTURES)
inline void QGestureManager::cleanupCachedGestures(QObject *target, Qt::GestureType type)
{
    const auto iter = m_objectGestures.find({target, type});
    if (iter == m_objectGestures.end())
        return;

    const QList<QGesture *> &gestures = iter.value();
    for (auto &e : m_obsoleteGestures) {
        for (QGesture *g : gestures)
            e -= g;
    }
    for (QGesture *g : gestures) {
        m_deletedRecognizers.remove(g);
        m_gestureToRecognizer.remove(g);
        m_maybeGestures.remove(g);
        m_activeGestures.remove(g);
        m_gestureOwners.remove(g);
        m_gestureTargets.remove(g);
        m_gesturesToDelete.insert(g);
    }

    m_objectGestures.erase(iter);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qgesturemanager.cpp, line 731, as _ZN15QGestureManager7recycleEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QGestureManager::recycle(QGesture *gesture)
{
    QGestureRecognizer *recognizer = m_gestureToRecognizer.value(gesture, 0);
    if (recognizer) {
        gesture->setGestureCancelPolicy(QGesture::CancelNone);
        recognizer->reset(gesture);
        m_activeGestures.remove(gesture);
    } else {
        cleanupGesturesForRemovedRecognizer(gesture);
    }
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qgesturemanager.cpp, line 463, as _ZN15QGestureManager35cleanupGesturesForRemovedRecognizerEP8QGesture
#if !defined(QT_NO_GESTURES)
inline void QGestureManager::cleanupGesturesForRemovedRecognizer(QGesture *gesture)
{
    QGestureRecognizer *recognizer = m_deletedRecognizers.value(gesture);
    if (!recognizer) //The Gesture is removed while in the even loop, so the recognizers for this gestures was removed
        return;
    m_deletedRecognizers.remove(gesture);
    if (m_deletedRecognizers.keys(recognizer).isEmpty()) {
        // no more active gestures, cleanup!
        qDeleteAll(m_obsoleteGestures.value(recognizer));
        m_obsoleteGestures.remove(recognizer);
        delete recognizer;
    }
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qgesturemanager.cpp, line 562, as _ZN15QGestureManager17getGestureTargetsERK4QSetIP8QGestureEP5QHashIP7QWidget5QListIS2_EESC_
#if !defined(QT_NO_GESTURES)
inline void QGestureManager::getGestureTargets(const QSet<QGesture*> &gestures,
    QHash<QWidget *, QList<QGesture *> > *conflicts,
    QHash<QWidget *, QList<QGesture *> > *normal)
{
    typedef QHash<Qt::GestureType, QHash<QWidget *, QGesture *> > GestureByTypes;
    GestureByTypes gestureByTypes;

    // sort gestures by types
    for (QGesture *gesture : gestures) {
        QWidget *receiver = m_gestureTargets.value(gesture, nullptr);
        Q_ASSERT(receiver);
        if (receiver)
            gestureByTypes[gesture->gestureType()].insert(receiver, gesture);
    }

    // for each gesture type
    for (GestureByTypes::const_iterator git = gestureByTypes.cbegin(), gend = gestureByTypes.cend(); git != gend; ++git) {
        const QHash<QWidget *, QGesture *> &gestures = git.value();
        for (QHash<QWidget *, QGesture *>::const_iterator wit = gestures.cbegin(), wend = gestures.cend(); wit != wend; ++wit) {
            QWidget *widget = wit.key();
            QWidget *w = widget->parentWidget();
            while (w) {
                QMap<Qt::GestureType, Qt::GestureFlags>::const_iterator it
                        = w->d_func()->gestureContext.constFind(git.key());
                if (it != w->d_func()->gestureContext.constEnd()) {
                    // i.e. 'w' listens to gesture 'type'
                    if (!(it.value() & Qt::DontStartGestureOnChildren) && w != widget) {
                        // conflicting gesture!
                        (*conflicts)[widget].append(wit.value());
                        break;
                    }
                }
                if (w->isWindow()) {
                    w = nullptr;
                    break;
                }
                w = w->parentWidget();
            }
            if (!w)
                (*normal)[widget].append(wit.value());
        }
    }
}
#endif  // !defined(QT_NO_GESTURES)
//  -----------------------------------------------------------------------

//  A QGestureManager that Python can take functions over in. Every QGestureManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGestureManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGestureManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGestureManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGestureManager : public QGestureManager {
public:
  using QGestureManager::QGestureManager;
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
      CuteQGestureManagerCall0 call = reinterpret_cast<CuteQGestureManagerCall0>(taken[0]);
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
      CuteQGestureManagerCall1 call = reinterpret_cast<CuteQGestureManagerCall1>(taken[1]);
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
      CuteQGestureManagerCall2 call = reinterpret_cast<CuteQGestureManagerCall2>(taken[2]);
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
      CuteQGestureManagerCall3 call = reinterpret_cast<CuteQGestureManagerCall3>(taken[3]);
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
      CuteQGestureManagerCall4 call = reinterpret_cast<CuteQGestureManagerCall4>(taken[4]);
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
      CuteQGestureManagerCall5 call = reinterpret_cast<CuteQGestureManagerCall5>(taken[5]);
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
      CuteQGestureManagerCall6 call = reinterpret_cast<CuteQGestureManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGestureManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGestureManager10metaObjectEv(
    const QGestureManager *self) {
  return self->metaObject();
}

//  void *QGestureManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGestureManager11qt_metacastEPKc(
    QGestureManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGestureManager::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGestureManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QGestureManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QGestureManager::~QGestureManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGestureManagerD1Ev(QGestureManager *self) {
  delete self;
}

#if !defined(QT_NO_GESTURES)
//  Qt::GestureType
//      QGestureManager::registerGestureRecognizer(QGestureRecognizer
//      *recognizer)
extern "C" Q_DECL_EXPORT
Qt::GestureType ritual_ZN15QGestureManager25registerGestureRecognizerEP18QGestureRecognizer(
    QGestureManager *self,
    QGestureRecognizer *recognizer) {
  return self->registerGestureRecognizer(recognizer);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QGestureManager::unregisterGestureRecognizer(Qt::GestureType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGestureManager27unregisterGestureRecognizerEN2Qt11GestureTypeE(
    QGestureManager *self,
    Qt::GestureType type) {
  self->unregisterGestureRecognizer(type);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QGestureManager::cleanupCachedGestures(QObject *target,
//      Qt::GestureType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGestureManager21cleanupCachedGesturesEP7QObjectN2Qt11GestureTypeE(
    QGestureManager *self,
    QObject *target,
    Qt::GestureType type) {
  self->cleanupCachedGestures(target, type);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QGestureManager::recycle(QGesture *gesture)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGestureManager7recycleEP8QGesture(
    QGestureManager *self,
    QGesture *gesture) {
  self->recycle(gesture);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QGestureManager::cleanupGesturesForRemovedRecognizer(QGesture
//      *gesture)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGestureManager35cleanupGesturesForRemovedRecognizerEP8QGesture(
    QGestureManager *self,
    QGesture *gesture) {
  self->cleanupGesturesForRemovedRecognizer(gesture);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QGestureManager::getGestureTargets(const QSet<QGesture *> &gestures,
//      QHash<QWidget *, QList<QGesture *>> *conflicts, QHash<QWidget *,
//      QList<QGesture *>> *normal)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGestureManager17getGestureTargetsERK4QSetIP8QGestureEP5QHashIP7QWidget5QListIS2_EESC_(
    QGestureManager *self,
    const QSet<QGesture *> *gestures,
    QHash<QWidget *, QList<QGesture *>> *conflicts,
    QHash<QWidget *, QList<QGesture *>> *normal) {
  self->getGestureTargets(*gestures, conflicts, normal);
}
#endif  // !defined(QT_NO_GESTURES)

//  a Python function taken by a CuteQGestureManager, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGestureManager(
    QGestureManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGestureManager *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_GESTURES)
