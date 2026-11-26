//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickrendercontrol.h>
#include <QtQml/qjsengine.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <QtQuick/private/qquickscreen_p.h>
#include <QtQuick/private/qquicksafearea_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qpen.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/qinputmethod.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQuick/private/qquickstategroup_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickaccessibleattached_p.h>
#include <QtQuick/private/qquickattachedpropertypropagator_p.h>
#include <QtQuick/private/qquickhoverhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickpointerhandler_p_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtCore/private/qdebug_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#if QT_CONFIG(cursor)
# include <QtGui/qcursor.h>
#endif
#if QT_CONFIG(accessibility)
# include <QtGui/private/qaccessiblecache_p.h>
#endif
#include <QtCore/qpointer.h>
#include <algorithm>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 312, as _ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb
inline void QQuickItemKeyFilter::keyPressed(QKeyEvent *event, bool post)
{
    if (m_next) m_next->keyPressed(event, post);
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 317, as _ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb
inline void QQuickItemKeyFilter::keyReleased(QKeyEvent *event, bool post)
{
    if (m_next) m_next->keyReleased(event, post);
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 323, as _ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEventb
#if QT_CONFIG(im)
inline void QQuickItemKeyFilter::inputMethodEvent(QInputMethodEvent *event, bool post)
{
    if (m_next)
        m_next->inputMethodEvent(event, post);
    else
        event->ignore();
}
#endif  // QT_CONFIG(im)

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 346, as _ZN19QQuickItemKeyFilter17componentCompleteEv
inline void QQuickItemKeyFilter::componentComplete()
{
    if (m_next) m_next->componentComplete();
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 338, as _ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent
inline void QQuickItemKeyFilter::shortcutOverrideEvent(QKeyEvent *event)
{
    if (m_next)
        m_next->shortcutOverrideEvent(event);
    else
        event->ignore();
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 308, as _ZN19QQuickItemKeyFilterD2Ev
inline QQuickItemKeyFilter::~QQuickItemKeyFilter()
{
}

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 331, as _ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMethodQueryE
#if QT_CONFIG(im)
inline QVariant QQuickItemKeyFilter::inputMethodQuery(Qt::InputMethodQuery query) const
{
    if (m_next) return m_next->inputMethodQuery(query);
    return QVariant();
}
#endif  // QT_CONFIG(im)

//  from ../qtdeclarative/src/quick/items/qquickitem.cpp, line 298, as _ZN19QQuickItemKeyFilterC1EP10QQuickItem
inline QQuickItemKeyFilter::QQuickItemKeyFilter(QQuickItem *item)
: m_processPost(false), m_next(nullptr)
{
    QQuickItemPrivate *p = item?QQuickItemPrivate::get(item):nullptr;
    if (p) {
        m_next = p->extra.value().keyHandler;
        p->extra->keyHandler = this;
    }
}
//  -----------------------------------------------------------------------

//  A QQuickItemKeyFilter that Python can take functions over in. Every QQuickItemKeyFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickItemKeyFilterCall0)(const void *, QKeyEvent *, bool, int *);
typedef void (*CuteQQuickItemKeyFilterCall1)(const void *, QKeyEvent *, bool, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickItemKeyFilterCall2)(const void *, QInputMethodEvent *, bool, int *);
#endif  // QT_CONFIG(im)
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickItemKeyFilterCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickItemKeyFilterCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickItemKeyFilterCall5)(const void *, int *);
class CuteQQuickItemKeyFilter : public QQuickItemKeyFilter {
public:
  using QQuickItemKeyFilter::QQuickItemKeyFilter;
  CuteQQuickItemKeyFilter(const QQuickItemKeyFilter & other) : QQuickItemKeyFilter(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEventb")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickItemKeyFilter17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QQuickItemKeyFilter::keyPressed(QKeyEvent *event, bool post)
  void keyPressed(QKeyEvent *event, bool post) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemKeyFilterCall0 call = reinterpret_cast<CuteQQuickItemKeyFilterCall0>(taken[0]);
      call(this, event, post, &handled);
      if (handled) return;
    }
    QQuickItemKeyFilter::keyPressed(event, post);
  }

  //  void QQuickItemKeyFilter::keyReleased(QKeyEvent *event, bool post)
  void keyReleased(QKeyEvent *event, bool post) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemKeyFilterCall1 call = reinterpret_cast<CuteQQuickItemKeyFilterCall1>(taken[1]);
      call(this, event, post, &handled);
      if (handled) return;
    }
    QQuickItemKeyFilter::keyReleased(event, post);
  }

#if QT_CONFIG(im)
  //  void QQuickItemKeyFilter::inputMethodEvent(QInputMethodEvent *event,
  //      bool post)
  void inputMethodEvent(QInputMethodEvent *event, bool post) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemKeyFilterCall2 call = reinterpret_cast<CuteQQuickItemKeyFilterCall2>(taken[2]);
      call(this, event, post, &handled);
      if (handled) return;
    }
    QQuickItemKeyFilter::inputMethodEvent(event, post);
  }
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
  //  QVariant QQuickItemKeyFilter::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemKeyFilterCall3 call = reinterpret_cast<CuteQQuickItemKeyFilterCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItemKeyFilter::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItemKeyFilter::shortcutOverrideEvent(QKeyEvent *event)
  void shortcutOverrideEvent(QKeyEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemKeyFilterCall4 call = reinterpret_cast<CuteQQuickItemKeyFilterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItemKeyFilter::shortcutOverrideEvent(event);
  }

  //  void QQuickItemKeyFilter::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemKeyFilterCall5 call = reinterpret_cast<CuteQQuickItemKeyFilterCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemKeyFilter::componentComplete();
  }
};

#if QT_CONFIG(im)
//  QQuickItemKeyFilter::QQuickItemKeyFilter(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
QQuickItemKeyFilter *ritual_ZN19QQuickItemKeyFilterC1EP10QQuickItem(
    QQuickItem *a0) {
  return new CuteQQuickItemKeyFilter(a0);
}
#endif  // QT_CONFIG(im)

//  QQuickItemKeyFilter::~QQuickItemKeyFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickItemKeyFilterD1Ev(QQuickItemKeyFilter *self) {
  delete self;
}

//  void QQuickItemKeyFilter::keyPressed(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb(
    QQuickItemKeyFilter *self,
    QKeyEvent *event,
    bool post) {
  self->keyPressed(event, post);
}

//  void QQuickItemKeyFilter::keyReleased(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb(
    QQuickItemKeyFilter *self,
    QKeyEvent *event,
    bool post) {
  self->keyReleased(event, post);
}

#if QT_CONFIG(im)
//  void QQuickItemKeyFilter::inputMethodEvent(QInputMethodEvent *event, bool
//      post)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEventb(
    QQuickItemKeyFilter *self,
    QInputMethodEvent *event,
    bool post) {
  self->inputMethodEvent(event, post);
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QQuickItemKeyFilter::inputMethodQuery(Qt::InputMethodQuery
//      query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickItemKeyFilter *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  void QQuickItemKeyFilter::shortcutOverrideEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent(
    QQuickItemKeyFilter *self,
    QKeyEvent *event) {
  self->shortcutOverrideEvent(event);
}

//  void QQuickItemKeyFilter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickItemKeyFilter17componentCompleteEv(
    QQuickItemKeyFilter *self) {
  self->componentComplete();
}

//  a Python function taken by a CuteQQuickItemKeyFilter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemKeyFilter(
    QQuickItemKeyFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemKeyFilter *>(self)->take(key, call);
}

//  void QQuickItemKeyFilter::keyPressed(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickItemKeyFilter10keyPressedEP9QKeyEventb(
    QQuickItemKeyFilter *self,
    QKeyEvent *event,
    bool post) {
  self->QQuickItemKeyFilter::keyPressed(event, post);
}

//  void QQuickItemKeyFilter::keyReleased(QKeyEvent *event, bool post)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickItemKeyFilter11keyReleasedEP9QKeyEventb(
    QQuickItemKeyFilter *self,
    QKeyEvent *event,
    bool post) {
  self->QQuickItemKeyFilter::keyReleased(event, post);
}

#if QT_CONFIG(im)
//  void QQuickItemKeyFilter::inputMethodEvent(QInputMethodEvent *event, bool
//      post)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickItemKeyFilter16inputMethodEventEP17QInputMethodEventb(
    QQuickItemKeyFilter *self,
    QInputMethodEvent *event,
    bool post) {
  self->QQuickItemKeyFilter::inputMethodEvent(event, post);
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QQuickItemKeyFilter::inputMethodQuery(Qt::InputMethodQuery
//      query) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QQuickItemKeyFilter16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickItemKeyFilter *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QQuickItemKeyFilter::inputMethodQuery(query));
}
#endif  // QT_CONFIG(im)

//  void QQuickItemKeyFilter::shortcutOverrideEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickItemKeyFilter21shortcutOverrideEventEP9QKeyEvent(
    QQuickItemKeyFilter *self,
    QKeyEvent *event) {
  self->QQuickItemKeyFilter::shortcutOverrideEvent(event);
}

//  void QQuickItemKeyFilter::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickItemKeyFilter17componentCompleteEv(
    QQuickItemKeyFilter *self) {
  self->QQuickItemKeyFilter::componentComplete();
}
