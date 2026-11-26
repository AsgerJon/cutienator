//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/qvalue3daxis_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QValue3DAxisPrivate' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qvalue3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qvalue3daxis_p.h>
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/abstract3dcontroller_p.h>
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QPainter>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qquaternion.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QRegularExpression>
#include <QtCore/QLocale>
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/qvalue3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__QValue3DAxisPrivate.cpp, line 1, as moc:QValue3DAxisPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN19QValue3DAxisPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QValue3DAxisPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN19QValue3DAxisPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QValue3DAxisPrivate",
        "formatterDirty",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'formatterDirty'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QValue3DAxisPrivate, qt_meta_tag_ZN19QValue3DAxisPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QValue3DAxisPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstract3DAxisPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QValue3DAxisPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QValue3DAxisPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN19QValue3DAxisPrivateE_t>.metaTypes,
    nullptr
} };

void QValue3DAxisPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QValue3DAxisPrivate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->formatterDirty(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QValue3DAxisPrivate::*)()>(_a, &QValue3DAxisPrivate::formatterDirty, 0))
            return;
    }
}

const QMetaObject *QValue3DAxisPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QValue3DAxisPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QValue3DAxisPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstract3DAxisPrivate::qt_metacast(_clname);
}

int QValue3DAxisPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstract3DAxisPrivate::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QValue3DAxisPrivate::formatterDirty()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 320, as _ZN19QValue3DAxisPrivate12updateLabelsEv
inline void QValue3DAxisPrivate::updateLabels()
{
    if (!m_labelsDirty)
        return;

    m_labelsDirty = false;

    m_formatter->d_ptr->recalculate();

    m_labels = m_formatter->labelStrings();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 337, as _ZN19QValue3DAxisPrivate14allowNegativesEv
inline bool QValue3DAxisPrivate::allowNegatives()
{
    return m_formatter->allowNegatives();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 342, as _ZN19QValue3DAxisPrivate15allowMinMaxSameEv
inline bool QValue3DAxisPrivate::allowMinMaxSame()
{
    return false;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 304, as _ZN19QValue3DAxisPrivate6setMaxEf
inline void QValue3DAxisPrivate::setMax(float max)
{
    bool dirty = (max != m_max);

    QAbstract3DAxisPrivate::setMax(max);

    if (dirty)
        emitLabelsChanged();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 294, as _ZN19QValue3DAxisPrivate6setMinEf
inline void QValue3DAxisPrivate::setMin(float min)
{
    bool dirty = (min != m_min);

    QAbstract3DAxisPrivate::setMin(min);

    if (dirty)
        emitLabelsChanged();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 284, as _ZN19QValue3DAxisPrivate8setRangeEffb
inline void QValue3DAxisPrivate::setRange(float min, float max, bool suppressWarnings)
{
    bool dirty = (min != m_min || max != m_max);

    QAbstract3DAxisPrivate::setRange(min, max, suppressWarnings);

    if (dirty)
        emitLabelsChanged();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 332, as _ZN19QValue3DAxisPrivate9allowZeroEv
inline bool QValue3DAxisPrivate::allowZero()
{
    return m_formatter->allowZero();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 280, as _ZN19QValue3DAxisPrivateD0Ev
inline QValue3DAxisPrivate::~QValue3DAxisPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 374, as _ZN22QAbstract3DAxisPrivateC2EP15QAbstract3DAxisNS0_8AxisTypeE
inline QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis *q, QAbstract3DAxis::AxisType type)
    : QObject(0),
      q_ptr(q),
      m_orientation(QAbstract3DAxis::AxisOrientationNone),
      m_type(type),
      m_isDefaultAxis(false),
      m_min(0.0f),
      m_max(10.0f),
      m_autoAdjust(true),
      m_labelAutoRotation(0.0f),
      m_titleVisible(false),
      m_titleFixed(true)
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 389, as _ZN22QAbstract3DAxisPrivateD2Ev
inline QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 279, as _ZN5Utils18defaultLabelFormatEv
inline QString Utils::defaultLabelFormat()
{
    static const QString defaultFormat(QStringLiteral("%.2f"));
    return defaultFormat;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 503, as _ZN22QAbstract3DAxisPrivate6setMaxEf
inline void QAbstract3DAxisPrivate::setMax(float max)
{
    if (!allowNegatives()) {
        if (allowZero()) {
            if (max < 0.0f) {
                max = 0.0f;
                qWarning() << "Warning: Tried to set negative maximum for an axis that only"
                              "supports positive values and zero:" << max;
            }
        } else {
            if (max <= 0.0f) {
                max = 1.0f;
                qWarning() << "Warning: Tried to set negative or zero maximum for an axis that only"
                              "supports positive values:" << max;
            }
        }
    }

    if (m_max != max) {
        bool minChanged = false;
        if (m_min > max || (!allowMinMaxSame() && m_min == max)) {
            float oldMin = m_min;
            m_min = max - 1.0f;
            if (!allowNegatives() && m_min < 0.0f) {
                if (allowZero())
                    m_min = 0.0f;
                else
                    m_min = max / 2.0f; // Need some positive value smaller than max

                if (!allowMinMaxSame() && max == 0.0f) {
                    m_min = oldMin;
                    qWarning() << "Unable to set maximum value to zero.";
                    return;
                }
            }
            qWarning() << "Warning: Tried to set maximum to equal or smaller than minimum for"
                          " value axis. Minimum automatically adjusted to a valid one:"
                       << oldMin <<  "-->" << m_min;
            minChanged = true;
        }
        m_max = max;
        emit q_ptr->rangeChanged(m_min, m_max);
        emit q_ptr->maxChanged(m_max);
        if (minChanged)
            emit q_ptr->minChanged(m_min);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 466, as _ZN22QAbstract3DAxisPrivate6setMinEf
inline void QAbstract3DAxisPrivate::setMin(float min)
{
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                qWarning() << "Warning: Tried to set negative minimum for an axis that only"
                              "supports positive values and zero:" << min;
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                qWarning() << "Warning: Tried to set negative or zero minimum for an axis that only"
                              "supports positive values:" << min;
            }
        }
    }

    if (m_min != min) {
        bool maxChanged = false;
        if (min > m_max || (!allowMinMaxSame() && min == m_max)) {
            float oldMax = m_max;
            m_max = min + 1.0f;
            qWarning() << "Warning: Tried to set minimum to equal or larger than maximum for"
                          " value axis. Maximum automatically adjusted to a valid one:"
                       << oldMax <<  "-->" << m_max;
            maxChanged = true;
        }
        m_min = min;

        emit q_ptr->rangeChanged(m_min, m_max);
        emit q_ptr->minChanged(m_min);
        if (maxChanged)
            emit q_ptr->maxChanged(m_max);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 408, as _ZN22QAbstract3DAxisPrivate8setRangeEffb
inline void QAbstract3DAxisPrivate::setRange(float min, float max, bool suppressWarnings)
{
    bool adjusted = false;
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                adjusted = true;
            }
            if (max < 0.0f) {
                max = 0.0f;
                adjusted = true;
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                adjusted = true;
            }
            if (max <= 0.0f) {
                max = 1.0f;
                adjusted = true;
            }
        }
    }
    // If min >= max, we adjust ranges so that
    // m_max becomes (min + 1.0f)
    // as axes need some kind of valid range.
    bool minDirty = false;
    bool maxDirty = false;
    if (m_min != min) {
        m_min = min;
        minDirty = true;
    }
    if (m_max != max || min > max || (!allowMinMaxSame() && min == max)) {
        if (min > max || (!allowMinMaxSame() && min == max)) {
            m_max = min + 1.0f;
            adjusted = true;
        } else {
            m_max = max;
        }
        maxDirty = true;
    }

    if (minDirty || maxDirty) {
        if (adjusted && !suppressWarnings) {
            qWarning() << "Warning: Tried to set invalid range for axis."
                          " Range automatically adjusted to a valid one:"
                       << min << "-" << max << "-->" << m_min << "-" << m_max;
        }
        emit q_ptr->rangeChanged(m_min, m_max);
    }

    if (minDirty)
        emit q_ptr->minChanged(m_min);
    if (maxDirty)
        emit q_ptr->maxChanged(m_max);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 311, as _ZN28QValue3DAxisFormatterPrivate11recalculateEv
inline void QValue3DAxisFormatterPrivate::recalculate()
{
    // Only recalculate if we need to and have m_axis pointer. If we do not have
    // m_axis, either we are not attached to an axis or this is a renderer cache.
    if (m_axis && m_needsRecalculate) {
        m_min = m_axis->min();
        m_max = m_axis->max();
        m_rangeNormalizer = (m_max - m_min);

        q_ptr->recalculate();
        m_needsRecalculate = false;
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 269, as _ZN19QValue3DAxisPrivateC1EP12QValue3DAxis
inline QValue3DAxisPrivate::QValue3DAxisPrivate(QValue3DAxis *q)
    : QAbstract3DAxisPrivate(q, QAbstract3DAxis::AxisTypeValue),
      m_segmentCount(5),
      m_subSegmentCount(1),
      m_labelFormat(Utils::defaultLabelFormat()),
      m_labelsDirty(true),
      m_formatter(0),
      m_reversed(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 314, as _ZN19QValue3DAxisPrivate17emitLabelsChangedEv
inline void QValue3DAxisPrivate::emitLabelsChanged()
{
    m_labelsDirty = true;
    emit q_ptr->labelsChanged();
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxis.cpp, line 347, as _ZN19QValue3DAxisPrivate4qptrEv
inline QValue3DAxis *QValue3DAxisPrivate::qptr()
{
    return static_cast<QValue3DAxis *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  Only a class built on QValue3DAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQValue3DAxisPrivate : QValue3DAxisPrivate {
  using QValue3DAxisPrivate::updateLabels;
  using QValue3DAxisPrivate::allowZero;
  using QValue3DAxisPrivate::allowNegatives;
  using QValue3DAxisPrivate::allowMinMaxSame;
};

//  A QValue3DAxisPrivate that Python can take functions over in. Every QValue3DAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQValue3DAxisPrivateCall0)(const void *, float, float, bool, int *);
typedef void (*CuteQValue3DAxisPrivateCall1)(const void *, float, int *);
typedef void (*CuteQValue3DAxisPrivateCall2)(const void *, float, int *);
typedef void (*CuteQValue3DAxisPrivateCall3)(const void *, int *);
typedef bool (*CuteQValue3DAxisPrivateCall4)(const void *, int *);
typedef bool (*CuteQValue3DAxisPrivateCall5)(const void *, int *);
typedef bool (*CuteQValue3DAxisPrivateCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisPrivateCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisPrivateCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisPrivateCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisPrivateCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisPrivateCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValue3DAxisPrivate : public QValue3DAxisPrivate {
public:
  using QValue3DAxisPrivate::QValue3DAxisPrivate;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate8setRangeEffb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMinEf")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMaxEf")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate12updateLabelsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate9allowZeroEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate14allowNegativesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QValue3DAxisPrivate::setRange(float min, float max, bool
  //      suppressWarnings)
  void setRange(float min, float max, bool suppressWarnings) override {
    if (taken[0]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall0 call = reinterpret_cast<CuteQValue3DAxisPrivateCall0>(taken[0]);
      call(this, min, max, suppressWarnings, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::setRange(min, max, suppressWarnings);
  }

  //  void QValue3DAxisPrivate::setMin(float min)
  void setMin(float min) override {
    if (taken[1]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall1 call = reinterpret_cast<CuteQValue3DAxisPrivateCall1>(taken[1]);
      call(this, min, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::setMin(min);
  }

  //  void QValue3DAxisPrivate::setMax(float max)
  void setMax(float max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall2 call = reinterpret_cast<CuteQValue3DAxisPrivateCall2>(taken[2]);
      call(this, max, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::setMax(max);
  }

  //  void QValue3DAxisPrivate::updateLabels()
  void updateLabels() override {
    if (taken[3]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall3 call = reinterpret_cast<CuteQValue3DAxisPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QValue3DAxisPrivate::updateLabels();
  }

  //  bool QValue3DAxisPrivate::allowZero()
  bool allowZero() override {
    if (taken[4]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall4 call = reinterpret_cast<CuteQValue3DAxisPrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QValue3DAxisPrivate::allowZero();
  }

  //  bool QValue3DAxisPrivate::allowNegatives()
  bool allowNegatives() override {
    if (taken[5]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall5 call = reinterpret_cast<CuteQValue3DAxisPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QValue3DAxisPrivate::allowNegatives();
  }

  //  bool QValue3DAxisPrivate::allowMinMaxSame()
  bool allowMinMaxSame() override {
    if (taken[6]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall6 call = reinterpret_cast<CuteQValue3DAxisPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QValue3DAxisPrivate::allowMinMaxSame();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall7 call = reinterpret_cast<CuteQValue3DAxisPrivateCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall8 call = reinterpret_cast<CuteQValue3DAxisPrivateCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall9 call = reinterpret_cast<CuteQValue3DAxisPrivateCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall10 call = reinterpret_cast<CuteQValue3DAxisPrivateCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall11 call = reinterpret_cast<CuteQValue3DAxisPrivateCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall12 call = reinterpret_cast<CuteQValue3DAxisPrivateCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQValue3DAxisPrivateCall13 call = reinterpret_cast<CuteQValue3DAxisPrivateCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValue3DAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QValue3DAxisPrivate10metaObjectEv(
    const QValue3DAxisPrivate *self) {
  return self->metaObject();
}

//  void *QValue3DAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QValue3DAxisPrivate11qt_metacastEPKc(
    QValue3DAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QValue3DAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QValue3DAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QValue3DAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QValue3DAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QValue3DAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValue3DAxisPrivate::tr(s, c, n));
}

//  QValue3DAxisPrivate::QValue3DAxisPrivate(QValue3DAxis *q)
extern "C" Q_DECL_EXPORT
QValue3DAxisPrivate *ritual_ZN19QValue3DAxisPrivateC1EP12QValue3DAxis(
    QValue3DAxis *q) {
  return new CuteQValue3DAxisPrivate(q);
}

//  QValue3DAxisPrivate::~QValue3DAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivateD1Ev(QValue3DAxisPrivate *self) {
  delete self;
}

//  void QValue3DAxisPrivate::setRange(float min, float max, bool
//      suppressWarnings)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate8setRangeEffb(
    QValue3DAxisPrivate *self,
    float min,
    float max,
    bool suppressWarnings) {
  self->setRange(min, max, suppressWarnings);
}

//  void QValue3DAxisPrivate::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate6setMinEf(
    QValue3DAxisPrivate *self,
    float min) {
  self->setMin(min);
}

//  void QValue3DAxisPrivate::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate6setMaxEf(
    QValue3DAxisPrivate *self,
    float max) {
  self->setMax(max);
}

//  void QValue3DAxisPrivate::emitLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate17emitLabelsChangedEv(
    QValue3DAxisPrivate *self) {
  self->emitLabelsChanged();
}

//  void QValue3DAxisPrivate::formatterDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate14formatterDirtyEv(
    QValue3DAxisPrivate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QValue3DAxisPrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "formatterDirty()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "formatterDirty()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QValue3DAxisPrivate::updateLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QValue3DAxisPrivate12updateLabelsEv(
    QValue3DAxisPrivate *self) {
  self->updateLabels();
}

//  bool QValue3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QValue3DAxisPrivate9allowZeroEv(QValue3DAxisPrivate *self) {
  return self->allowZero();
}

//  bool QValue3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QValue3DAxisPrivate14allowNegativesEv(
    QValue3DAxisPrivate *self) {
  return self->allowNegatives();
}

//  bool QValue3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QValue3DAxisPrivate15allowMinMaxSameEv(
    QValue3DAxisPrivate *self) {
  return self->allowMinMaxSame();
}

//  QValue3DAxis *QValue3DAxisPrivate::qptr()
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZN19QValue3DAxisPrivate4qptrEv(
    QValue3DAxisPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQValue3DAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValue3DAxisPrivate(
    QValue3DAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValue3DAxisPrivate *>(self)->take(key, call);
}

//  void QValue3DAxisPrivate::setRange(float min, float max, bool
//      suppressWarnings)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QValue3DAxisPrivate8setRangeEffb(
    QValue3DAxisPrivate *self,
    float min,
    float max,
    bool suppressWarnings) {
  self->QValue3DAxisPrivate::setRange(min, max, suppressWarnings);
}

//  void QValue3DAxisPrivate::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QValue3DAxisPrivate6setMinEf(
    QValue3DAxisPrivate *self,
    float min) {
  self->QValue3DAxisPrivate::setMin(min);
}

//  void QValue3DAxisPrivate::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QValue3DAxisPrivate6setMaxEf(
    QValue3DAxisPrivate *self,
    float max) {
  self->QValue3DAxisPrivate::setMax(max);
}

//  void QValue3DAxisPrivate::updateLabels()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QValue3DAxisPrivate12updateLabelsEv(
    QValue3DAxisPrivate *self) {
  static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::updateLabels();
}

//  bool QValue3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QValue3DAxisPrivate9allowZeroEv(
    QValue3DAxisPrivate *self) {
  return static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::allowZero();
}

//  bool QValue3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QValue3DAxisPrivate14allowNegativesEv(
    QValue3DAxisPrivate *self) {
  return static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::allowNegatives();
}

//  bool QValue3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QValue3DAxisPrivate15allowMinMaxSameEv(
    QValue3DAxisPrivate *self) {
  return static_cast<OwnQValue3DAxisPrivate *>(self)->OwnQValue3DAxisPrivate::allowMinMaxSame();
}
