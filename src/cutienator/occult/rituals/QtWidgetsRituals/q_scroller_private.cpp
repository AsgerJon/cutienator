//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qscroller_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QScrollerPrivate' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scroller)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qscroller.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qscroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qscroller.h>
#include <QtWidgets/private/qflickgesture_p.h>
#include <QtWidgets/private/qscroller_p.h>
#include <QtWidgets/qscrollerproperties.h>
#include <QtWidgets/private/qscrollerproperties_p.h>
#include <QtCore/qnumeric.h>
#include "math.h"
#include <QtCore/QTime>
#include <QtCore/QElapsedTimer>
#include <QtCore/QMap>
#include <QtWidgets/QApplication>
#include <QtWidgets/QAbstractScrollArea>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/QGraphicsObject>
#include <QtWidgets/QGraphicsScene>
#include <QtWidgets/QGraphicsView>
#endif
#include <QtGui/QVector2D>
#include <QtCore/qmath.h>
#include <QtGui/qevent.h>
#include <QtCore/qnumeric.h>
#include <QtCore/QtDebug>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/util/qscroller.cpp, line 155, as local:qscroller.cpp:QScrollTimer
#if QT_CONFIG(animation)
class QScrollTimer : public QAbstractAnimation
{
public:
    QScrollTimer(QScrollerPrivate *_d) : QAbstractAnimation(_d), d(_d), skip(0) {}

    int duration() const override
    {
        return -1;
    }

    void start()
    {
        QAbstractAnimation::start();
        skip = 0;
    }

protected:
    void updateCurrentTime(int /*currentTime*/) override
   {
        if (++skip >= d->frameRateSkip()) {
            skip = 0;
            d->timerTick();
        }
    }

private:
    QScrollerPrivate *d;
    int skip;
};
#endif  // QT_CONFIG(animation)

//  from QtWidgets__QScrollerPrivate.cpp, line 1, as moc:QScrollerPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16QScrollerPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QScrollerPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN16QScrollerPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QScrollerPrivate",
        "targetDestroyed",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'targetDestroyed'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QScrollerPrivate, qt_meta_tag_ZN16QScrollerPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QScrollerPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QScrollerPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QScrollerPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16QScrollerPrivateE_t>.metaTypes,
    nullptr
} };

void QScrollerPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QScrollerPrivate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->targetDestroyed(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QScrollerPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QScrollerPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QScrollerPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QScrollerPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 1)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 1)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from src/widgets/util/qscroller.cpp, line 887, as _ZN16QScrollerPrivate15targetDestroyedEv
inline void QScrollerPrivate::targetDestroyed()
{
#if QT_CONFIG(animation)
    scrollTimer->stop();
#endif
    delete q_ptr;
}

//  from src/widgets/util/qscroller.cpp, line 895, as _ZN16QScrollerPrivate9timerTickEv
inline void QScrollerPrivate::timerTick()
{
    struct timerevent {
        QScroller::State state;
        typedef void (QScrollerPrivate::*timerhandler_t)();
        timerhandler_t handler;
    };

    timerevent timerevents[] = {
        { QScroller::Dragging, &QScrollerPrivate::timerEventWhileDragging },
        { QScroller::Scrolling, &QScrollerPrivate::timerEventWhileScrolling },
    };

    for (int i = 0; i < int(sizeof(timerevents) / sizeof(*timerevents)); ++i) {
        timerevent *te = timerevents + i;

        if (state == te->state) {
            (this->*te->handler)();
            return;
        }
    }

#if QT_CONFIG(animation)
    scrollTimer->stop();
#endif
}

//  from src/widgets/util/qscroller.cpp, line 855, as _ZN16QScrollerPrivate4initEv
inline void QScrollerPrivate::init()
{
    setDpiFromWidget(nullptr);
    monotonicTimer.start();
}

//  from src/widgets/util/qscroller.cpp, line 968, as _ZNK16QScrollerPrivate3dpiEv
inline QPointF QScrollerPrivate::dpi() const
{
    return pixelPerMeter * qreal(0.0254);
}

//  from src/widgets/util/qscroller.cpp, line 979, as _ZN16QScrollerPrivate6setDpiERK7QPointF
inline void QScrollerPrivate::setDpi(const QPointF &dpi)
{
    pixelPerMeter = dpi / qreal(0.0254);
}

//  from src/widgets/util/qscroller.cpp, line 987, as _ZN16QScrollerPrivate16setDpiFromWidgetEP7QWidget
inline void QScrollerPrivate::setDpiFromWidget(QWidget *widget)
{
    const QScreen *screen = widget ? widget->screen() : QGuiApplication::primaryScreen();
    Q_ASSERT(screen);
    setDpi(QPointF(screen->physicalDotsPerInchX(), screen->physicalDotsPerInchY()));
}

//  from src/widgets/util/qscroller.cpp, line 1095, as _ZNK16QScrollerPrivate23scrollingSegmentsEndPosEN2Qt11OrientationE
inline qreal QScrollerPrivate::scrollingSegmentsEndPos(Qt::Orientation orientation) const
{
    if (orientation == Qt::Horizontal) {
        if (xSegments.isEmpty())
            return contentPosition.x() + overshootPosition.x();
        else
            return xSegments.last().stopPos;
    } else {
        if (ySegments.isEmpty())
            return contentPosition.y() + overshootPosition.y();
        else
            return ySegments.last().stopPos;
    }
}

//  from src/widgets/util/qscroller.cpp, line 1113, as _ZNK16QScrollerPrivate22scrollingSegmentsValidEN2Qt11OrientationE
inline bool QScrollerPrivate::scrollingSegmentsValid(Qt::Orientation orientation) const
{
    const QQueue<ScrollSegment> *segments;
    qreal minPos;
    qreal maxPos;

    if (orientation == Qt::Horizontal) {
        segments = &xSegments;
        minPos = contentPosRange.left();
        maxPos = contentPosRange.right();
    } else {
        segments = &ySegments;
        minPos = contentPosRange.top();
        maxPos = contentPosRange.bottom();
    }

    if (segments->isEmpty())
        return true;

    const ScrollSegment &last = segments->last();
    qreal stopPos = last.stopPos;

    if (last.type == ScrollTypeScrollTo)
        return true; // scrollTo is always valid

    if (last.type == ScrollTypeOvershoot &&
        (stopPos != minPos && stopPos != maxPos))
        return false;

    if (stopPos < minPos || stopPos > maxPos)
        return false;

    if (stopPos == minPos || stopPos == maxPos) // the begin and the end of the list are always ok
        return true;

    qreal nextSnap = nextSnapPos(stopPos, 0, orientation);
    if (!qIsNaN(nextSnap) && stopPos != nextSnap)
        return false;

    return true;
}

//  from src/widgets/util/qscroller.cpp, line 1848, as _ZNK16QScrollerPrivate11nextSnapPosEdiN2Qt11OrientationE
inline qreal QScrollerPrivate::nextSnapPos(qreal p, int dir, Qt::Orientation orientation) const
{
    qreal bestSnapPos = Q_QNAN;
    qreal bestSnapPosDist = Q_INFINITY;

    qreal minPos;
    qreal maxPos;

    if (orientation == Qt::Horizontal) {
        minPos = contentPosRange.left();
        maxPos = contentPosRange.right();
    } else {
        minPos = contentPosRange.top();
        maxPos = contentPosRange.bottom();
    }

    if (orientation == Qt::Horizontal) {
        // the snap points in the list
        for (qreal snapPos : snapPositionsX) {
            qreal snapPosDist = snapPos - p;
            if ((dir > 0 && snapPosDist < 0) ||
                (dir < 0 && snapPosDist > 0))
                continue; // wrong direction
            if (snapPos < minPos || snapPos > maxPos )
                continue; // invalid

            if (qIsNaN(bestSnapPos) ||
                qAbs(snapPosDist) < bestSnapPosDist ) {
                bestSnapPos = snapPos;
                bestSnapPosDist = qAbs(snapPosDist);
            }
        }

        // the snap point interval
        if (snapIntervalX > 0.0) {
            qreal first = minPos + snapFirstX;
            qreal snapPos;
            if (dir > 0)
                snapPos = qCeil((p - first) / snapIntervalX) * snapIntervalX + first;
            else if (dir < 0)
                snapPos = qFloor((p - first) / snapIntervalX) * snapIntervalX + first;
            else if (p <= first)
                snapPos = first;
            else
            {
                qreal last = qFloor((maxPos - first) / snapIntervalX) * snapIntervalX + first;
                if (p >= last)
                    snapPos = last;
                else
                    snapPos = qRound((p - first) / snapIntervalX) * snapIntervalX + first;
            }

            if (snapPos >= first && snapPos <= maxPos ) {
                qreal snapPosDist = snapPos - p;

                if (qIsNaN(bestSnapPos) ||
                    qAbs(snapPosDist) < bestSnapPosDist ) {
                    bestSnapPos = snapPos;
                    bestSnapPosDist = qAbs(snapPosDist);
                }
            }
        }

    } else { // (orientation == Qt::Vertical)
        // the snap points in the list
        for (qreal snapPos : snapPositionsY) {
            qreal snapPosDist = snapPos - p;
            if ((dir > 0 && snapPosDist < 0) ||
                (dir < 0 && snapPosDist > 0))
                continue; // wrong direction
            if (snapPos < minPos || snapPos > maxPos )
                continue; // invalid

            if (qIsNaN(bestSnapPos) ||
                qAbs(snapPosDist) < bestSnapPosDist) {
                bestSnapPos = snapPos;
                bestSnapPosDist = qAbs(snapPosDist);
            }
        }

        // the snap point interval
        if (snapIntervalY > 0.0) {
            qreal first = minPos + snapFirstY;
            qreal snapPos;
            if (dir > 0)
                snapPos = qCeil((p - first) / snapIntervalY) * snapIntervalY + first;
            else if (dir < 0)
                snapPos = qFloor((p - first) / snapIntervalY) * snapIntervalY + first;
            else if (p <= first)
                snapPos = first;
            else
            {
                qreal last = qFloor((maxPos - first) / snapIntervalY) * snapIntervalY + first;
                if (p >= last)
                    snapPos = last;
                else
                    snapPos = qRound((p - first) / snapIntervalY) * snapIntervalY + first;
            }

            if (snapPos >= first && snapPos <= maxPos ) {
                qreal snapPosDist = snapPos - p;

                if (qIsNaN(bestSnapPos) ||
                    qAbs(snapPosDist) < bestSnapPosDist) {
                    bestSnapPos = snapPos;
                    bestSnapPosDist = qAbs(snapPosDist);
                }
            }
        }
    }

    return bestSnapPos;
}

//  from src/widgets/util/qscroller.cpp, line 1788, as _ZN16QScrollerPrivate19nextSegmentPositionER6QQueueINS_13ScrollSegmentEExd
inline qreal QScrollerPrivate::nextSegmentPosition(QQueue<ScrollSegment> &segments, qint64 now, qreal oldPos)
{
    qreal pos = oldPos;

    // check the X segments for new positions
    while (!segments.isEmpty()) {
        const ScrollSegment s = segments.head();

        if ((s.startTime + s.deltaTime * s.stopProgress) <= now) {
            segments.dequeue();
            pos = s.stopPos;
        } else if (s.startTime <= now) {
            qreal progress = qreal(now - s.startTime) / qreal(s.deltaTime);
            pos = s.startPos + s.deltaPos * s.curve.valueForProgress(progress);
            if (s.deltaPos > 0 ? pos > s.stopPos : pos < s.stopPos) {
                segments.dequeue();
                pos = s.stopPos;
            } else {
                break;
            }
        } else {
            break;
        }
    }
    return pos;
}

//  from src/widgets/util/qscroller.cpp, line 866, as _ZN16QScrollerPrivate9stateNameEN9QScroller5StateE
inline const char *QScrollerPrivate::stateName(QScroller::State state)
{
    switch (state) {
    case QScroller::Inactive:  return "inactive";
    case QScroller::Pressed:   return "pressed";
    case QScroller::Dragging:  return "dragging";
    case QScroller::Scrolling: return "scrolling";
    default:                   return "(invalid)";
    }
}

//  from src/widgets/util/qscroller.cpp, line 877, as _ZN16QScrollerPrivate9inputNameEN9QScroller5InputE
inline const char *QScrollerPrivate::inputName(QScroller::Input input)
{
    switch (input) {
    case QScroller::InputPress:   return "press";
    case QScroller::InputMove:    return "move";
    case QScroller::InputRelease: return "release";
    default:                      return "(invalid)";
    }
}
//  -----------------------------------------------------------------------

//  A QScrollerPrivate that Python can take functions over in. Every QScrollerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScrollerPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScrollerPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollerPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollerPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollerPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollerPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScrollerPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScrollerPrivate : public QScrollerPrivate {
public:
  using QScrollerPrivate::QScrollerPrivate;
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
      CuteQScrollerPrivateCall0 call = reinterpret_cast<CuteQScrollerPrivateCall0>(taken[0]);
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
      CuteQScrollerPrivateCall1 call = reinterpret_cast<CuteQScrollerPrivateCall1>(taken[1]);
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
      CuteQScrollerPrivateCall2 call = reinterpret_cast<CuteQScrollerPrivateCall2>(taken[2]);
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
      CuteQScrollerPrivateCall3 call = reinterpret_cast<CuteQScrollerPrivateCall3>(taken[3]);
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
      CuteQScrollerPrivateCall4 call = reinterpret_cast<CuteQScrollerPrivateCall4>(taken[4]);
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
      CuteQScrollerPrivateCall5 call = reinterpret_cast<CuteQScrollerPrivateCall5>(taken[5]);
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
      CuteQScrollerPrivateCall6 call = reinterpret_cast<CuteQScrollerPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScrollerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QScrollerPrivate10metaObjectEv(
    const QScrollerPrivate *self) {
  return self->metaObject();
}

//  void *QScrollerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QScrollerPrivate11qt_metacastEPKc(
    QScrollerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScrollerPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QScrollerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QScrollerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScrollerPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QScrollerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScrollerPrivate::tr(s, c, n));
}

//  QScroller *QScrollerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScroller *ritual_ZN16QScrollerPrivate6q_funcEv(QScrollerPrivate *self) {
  return self->q_func();
}

//  const QScroller *QScrollerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScroller *ritual_ZNK16QScrollerPrivate6q_funcEv(
    const QScrollerPrivate *self) {
  return self->q_func();
}

//  void QScrollerPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScrollerPrivate4initEv(QScrollerPrivate *self) {
  self->init();
}

//  QPointF QScrollerPrivate::dpi() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QScrollerPrivate3dpiEv(const QScrollerPrivate *self) {
  return new QPointF(self->dpi());
}

//  void QScrollerPrivate::setDpi(const QPointF &dpi)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScrollerPrivate6setDpiERK7QPointF(
    QScrollerPrivate *self,
    const QPointF *dpi) {
  self->setDpi(*dpi);
}

//  void QScrollerPrivate::setDpiFromWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScrollerPrivate16setDpiFromWidgetEP7QWidget(
    QScrollerPrivate *self,
    QWidget *widget) {
  self->setDpiFromWidget(widget);
}

//  qreal QScrollerPrivate::scrollingSegmentsEndPos(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QScrollerPrivate23scrollingSegmentsEndPosEN2Qt11OrientationE(
    const QScrollerPrivate *self,
    Qt::Orientation orientation) {
  return self->scrollingSegmentsEndPos(orientation);
}

//  bool QScrollerPrivate::scrollingSegmentsValid(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QScrollerPrivate22scrollingSegmentsValidEN2Qt11OrientationE(
    const QScrollerPrivate *self,
    Qt::Orientation orientation) {
  return self->scrollingSegmentsValid(orientation);
}

//  qreal QScrollerPrivate::nextSnapPos(qreal p, int dir, Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QScrollerPrivate11nextSnapPosEdiN2Qt11OrientationE(
    const QScrollerPrivate *self,
    qreal p,
    int dir,
    Qt::Orientation orientation) {
  return self->nextSnapPos(p, dir, orientation);
}

//  qreal QScrollerPrivate::nextSegmentPosition(QQueue<ScrollSegment>
//      &segments, qint64 now, qreal oldPos)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN16QScrollerPrivate19nextSegmentPositionER6QQueueINS_13ScrollSegmentEExd(
    QQueue<QScrollerPrivate::ScrollSegment> *segments,
    qint64 now,
    qreal oldPos) {
  return QScrollerPrivate::nextSegmentPosition(*segments, now, oldPos);
}

//  int QScrollerPrivate::frameRateSkip() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QScrollerPrivate13frameRateSkipEv(
    const QScrollerPrivate *self) {
  return self->frameRateSkip();
}

//  const char *QScrollerPrivate::stateName(QScroller::State state)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN16QScrollerPrivate9stateNameEN9QScroller5StateE(
    QScroller::State state) {
  return QScrollerPrivate::stateName(state);
}

//  const char *QScrollerPrivate::inputName(QScroller::Input input)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN16QScrollerPrivate9inputNameEN9QScroller5InputE(
    QScroller::Input input) {
  return QScrollerPrivate::inputName(input);
}

//  void QScrollerPrivate::targetDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScrollerPrivate15targetDestroyedEv(QScrollerPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScrollerPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "targetDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "targetDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQScrollerPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScrollerPrivate(
    QScrollerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScrollerPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(scroller)
