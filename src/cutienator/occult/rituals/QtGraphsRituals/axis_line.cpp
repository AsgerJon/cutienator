//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisline_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'AxisLine' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 7 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/axisline_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGraphs/private/axisline_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGraphs__AxisLine.cpp, line 1, as moc:AxisLine
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN8AxisLineE_t {};
} // unnamed namespace

template <> constexpr inline auto AxisLine::qt_create_metaobjectdata<qt_meta_tag_ZN8AxisLineE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AxisLine",
        "iResolutionChanged",
        "",
        "smoothingChanged",
        "colorChanged",
        "lineWidthChanged",
        "isHorizontalChanged",
        "iResolution",
        "QVector3D",
        "smoothing",
        "color",
        "QColor",
        "lineWidth",
        "isHorizontal"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'iResolutionChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'smoothingChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'colorChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'lineWidthChanged'
        QtMocHelpers::SignalData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'isHorizontalChanged'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'iResolution'
        QtMocHelpers::PropertyData<QVector3D>(7, 0x80000000 | 8, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 0),
        // property 'smoothing'
        QtMocHelpers::PropertyData<qreal>(9, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 1),
        // property 'color'
        QtMocHelpers::PropertyData<QColor>(10, 0x80000000 | 11, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 2),
        // property 'lineWidth'
        QtMocHelpers::PropertyData<qreal>(12, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 3),
        // property 'isHorizontal'
        QtMocHelpers::PropertyData<bool>(13, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 4),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AxisLine, qt_meta_tag_ZN8AxisLineE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AxisLine::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickShaderEffect::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8AxisLineE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8AxisLineE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN8AxisLineE_t>.metaTypes,
    nullptr
} };

void AxisLine::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AxisLine *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->iResolutionChanged(); break;
        case 1: _t->smoothingChanged(); break;
        case 2: _t->colorChanged(); break;
        case 3: _t->lineWidthChanged(); break;
        case 4: _t->isHorizontalChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (AxisLine::*)()>(_a, &AxisLine::iResolutionChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisLine::*)()>(_a, &AxisLine::smoothingChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisLine::*)()>(_a, &AxisLine::colorChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisLine::*)()>(_a, &AxisLine::lineWidthChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (AxisLine::*)()>(_a, &AxisLine::isHorizontalChanged, 4))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QVector3D*>(_v) = _t->iResolution(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->smoothing(); break;
        case 2: *reinterpret_cast<QColor*>(_v) = _t->color(); break;
        case 3: *reinterpret_cast<qreal*>(_v) = _t->lineWidth(); break;
        case 4: *reinterpret_cast<bool*>(_v) = _t->isHorizontal(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setSmoothing(*reinterpret_cast<qreal*>(_v)); break;
        case 2: _t->setColor(*reinterpret_cast<QColor*>(_v)); break;
        case 3: _t->setLineWidth(*reinterpret_cast<qreal*>(_v)); break;
        case 4: _t->setIsHorizontal(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *AxisLine::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AxisLine::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8AxisLineE_t>.strings))
        return static_cast<void*>(this);
    return QQuickShaderEffect::qt_metacast(_clname);
}

int AxisLine::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickShaderEffect::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 5;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void AxisLine::iResolutionChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void AxisLine::smoothingChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void AxisLine::colorChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void AxisLine::lineWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void AxisLine::isHorizontalChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}
QT_WARNING_POP

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 24, as _ZN8AxisLine14geometryChangeERK6QRectFS2_
inline void AxisLine::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    m_iResolution = QVector3D(newGeometry.width(), newGeometry.height(), 1.0);
    emit iResolutionChanged();

    QQuickShaderEffect::geometryChange(newGeometry, oldGeometry);
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 18, as _ZN8AxisLine17componentCompleteEv
inline void AxisLine::componentComplete()
{
    QQuickShaderEffect::componentComplete();
    setupShaders();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 16, as _ZN8AxisLineD0Ev
inline AxisLine::~AxisLine() {}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 10, as _ZN8AxisLineC1EP10QQuickItem
inline AxisLine::AxisLine(QQuickItem *parent) :
      QQuickShaderEffect(parent)
{

}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 32, as _ZN8AxisLine12setupShadersEv
inline void AxisLine::setupShaders()
{
    if (m_isHorizontal) {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/lineshaderhorizontal.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/lineshaderhorizontal.vert.qsb")));
    } else {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/lineshadervertical.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/lineshadervertical.vert.qsb")));
    }
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 43, as _ZNK8AxisLine11iResolutionEv
inline QVector3D AxisLine::iResolution() const
{
    return m_iResolution;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 48, as _ZNK8AxisLine9smoothingEv
inline qreal AxisLine::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 53, as _ZN8AxisLine12setSmoothingEd
inline void AxisLine::setSmoothing(qreal newSmoothing)
{
    if (QtPrivate::fuzzyCompare(m_smoothing, newSmoothing))
        return;
    m_smoothing = newSmoothing;
    emit smoothingChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 61, as _ZNK8AxisLine5colorEv
inline QColor AxisLine::color() const
{
    return m_color;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 66, as _ZN8AxisLine8setColorE6QColor
inline void AxisLine::setColor(QColor newColor)
{
    if (m_color == newColor)
        return;
    m_color = newColor;
    emit colorChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 74, as _ZNK8AxisLine9lineWidthEv
inline qreal AxisLine::lineWidth() const
{
    return m_lineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 79, as _ZN8AxisLine12setLineWidthEd
inline void AxisLine::setLineWidth(qreal newLineWidth)
{
    if (QtPrivate::fuzzyCompare(m_lineWidth, newLineWidth))
        return;
    m_lineWidth = newLineWidth;
    emit lineWidthChanged();
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 87, as _ZNK8AxisLine12isHorizontalEv
inline bool AxisLine::isHorizontal() const
{
    return m_isHorizontal;
}

//  from ../qtgraphs/src/graphs2d/axis/axisline.cpp, line 92, as _ZN8AxisLine15setIsHorizontalEb
inline void AxisLine::setIsHorizontal(bool newIsHorizontal)
{
    if (m_isHorizontal == newIsHorizontal)
        return;
    m_isHorizontal = newIsHorizontal;
    emit isHorizontalChanged();
}
//  -----------------------------------------------------------------------

//  Only a class built on AxisLine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAxisLine : AxisLine {
  using AxisLine::componentComplete;
  using AxisLine::geometryChange;
};

//  A AxisLine that Python can take functions over in. Every AxisLine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAxisLineCall0)(const void *, int *);
typedef void (*CuteAxisLineCall1)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteAxisLineCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteAxisLineCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteAxisLineCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteAxisLineCall5)(const void *, int *);
typedef const QRectF * (*CuteAxisLineCall6)(const void *, int *);
typedef bool (*CuteAxisLineCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAxisLineCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAxisLineCall9)(const void *, int *);
typedef void * (*CuteAxisLineCall10)(const void *, int *);
typedef void (*CuteAxisLineCall11)(const void *, int *);
typedef void (*CuteAxisLineCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteAxisLineCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAxisLineCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAxisLineCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisLineCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisLineCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisLineCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisLineCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisLineCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisLineCall21)(const void *, int *);
typedef void (*CuteAxisLineCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAxisLineCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAxisLineCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteAxisLineCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisLineCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisLineCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisLineCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisLineCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisLineCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisLineCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAxisLineCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteAxisLineCall33)(const void *, int *);
typedef void (*CuteAxisLineCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisLineCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisLineCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisLineCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisLineCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisLineCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisLineCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisLine : public AxisLine {
public:
  using AxisLine::AxisLine;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void AxisLine::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisLineCall0 call = reinterpret_cast<CuteAxisLineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    AxisLine::componentComplete();
  }

  //  void AxisLine::geometryChange(const QRectF &newGeometry, const QRectF
  //      &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisLineCall1 call = reinterpret_cast<CuteAxisLineCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    AxisLine::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffect::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisLineCall2 call = reinterpret_cast<CuteAxisLineCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickShaderEffect::event(e);
  }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_shadereffect)
  //  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *updatePaintNodeData)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *updatePaintNodeData) override {
    if (taken[3]) {
      int handled = 0;
      CuteAxisLineCall3 call = reinterpret_cast<CuteAxisLineCall3>(taken[3]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShaderEffect::updatePaintNode(oldNode, updatePaintNodeData);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffect::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteAxisLineCall4 call = reinterpret_cast<CuteAxisLineCall4>(taken[4]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickShaderEffect::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteAxisLineCall5 call = reinterpret_cast<CuteAxisLineCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteAxisLineCall6 call = reinterpret_cast<CuteAxisLineCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteAxisLineCall7 call = reinterpret_cast<CuteAxisLineCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteAxisLineCall8 call = reinterpret_cast<CuteAxisLineCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteAxisLineCall9 call = reinterpret_cast<CuteAxisLineCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAxisLineCall10 call = reinterpret_cast<CuteAxisLineCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteAxisLineCall11 call = reinterpret_cast<CuteAxisLineCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAxisLineCall12 call = reinterpret_cast<CuteAxisLineCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteAxisLineCall13 call = reinterpret_cast<CuteAxisLineCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteAxisLineCall14 call = reinterpret_cast<CuteAxisLineCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteAxisLineCall15 call = reinterpret_cast<CuteAxisLineCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteAxisLineCall16 call = reinterpret_cast<CuteAxisLineCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAxisLineCall17 call = reinterpret_cast<CuteAxisLineCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAxisLineCall18 call = reinterpret_cast<CuteAxisLineCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAxisLineCall19 call = reinterpret_cast<CuteAxisLineCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteAxisLineCall20 call = reinterpret_cast<CuteAxisLineCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAxisLineCall21 call = reinterpret_cast<CuteAxisLineCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteAxisLineCall22 call = reinterpret_cast<CuteAxisLineCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteAxisLineCall23 call = reinterpret_cast<CuteAxisLineCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteAxisLineCall24 call = reinterpret_cast<CuteAxisLineCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAxisLineCall25 call = reinterpret_cast<CuteAxisLineCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAxisLineCall26 call = reinterpret_cast<CuteAxisLineCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteAxisLineCall27 call = reinterpret_cast<CuteAxisLineCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteAxisLineCall28 call = reinterpret_cast<CuteAxisLineCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteAxisLineCall29 call = reinterpret_cast<CuteAxisLineCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteAxisLineCall30 call = reinterpret_cast<CuteAxisLineCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteAxisLineCall31 call = reinterpret_cast<CuteAxisLineCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteAxisLineCall32 call = reinterpret_cast<CuteAxisLineCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAxisLineCall33 call = reinterpret_cast<CuteAxisLineCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAxisLineCall34 call = reinterpret_cast<CuteAxisLineCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteAxisLineCall35 call = reinterpret_cast<CuteAxisLineCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteAxisLineCall36 call = reinterpret_cast<CuteAxisLineCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteAxisLineCall37 call = reinterpret_cast<CuteAxisLineCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteAxisLineCall38 call = reinterpret_cast<CuteAxisLineCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteAxisLineCall39 call = reinterpret_cast<CuteAxisLineCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteAxisLineCall40 call = reinterpret_cast<CuteAxisLineCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisLine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8AxisLine10metaObjectEv(const AxisLine *self) {
  return self->metaObject();
}

//  void *AxisLine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8AxisLine11qt_metacastEPKc(AxisLine *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int AxisLine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8AxisLine11qt_metacallEN11QMetaObject4CallEiPPv(
    AxisLine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AxisLine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8AxisLine2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(AxisLine::tr(s, c, n));
}

//  AxisLine::AxisLine(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
AxisLine *ritual_ZN8AxisLineC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteAxisLine(parent);
}

//  AxisLine::~AxisLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLineD1Ev(AxisLine *self) {
  delete self;
}

//  void AxisLine::setupShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine12setupShadersEv(AxisLine *self) {
  self->setupShaders();
}

//  QVector3D AxisLine::iResolution() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8AxisLine11iResolutionEv(const AxisLine *self) {
  return new QVector3D(self->iResolution());
}

//  qreal AxisLine::smoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisLine9smoothingEv(const AxisLine *self) {
  return self->smoothing();
}

//  void AxisLine::setSmoothing(qreal newSmoothing)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine12setSmoothingEd(AxisLine *self, qreal newSmoothing) {
  self->setSmoothing(newSmoothing);
}

//  QColor AxisLine::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisLine5colorEv(const AxisLine *self) {
  return new QColor(self->color());
}

//  void AxisLine::setColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine8setColorE6QColor(
    AxisLine *self,
    const QColor *newColor) {
  self->setColor(*newColor);
}

//  qreal AxisLine::lineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisLine9lineWidthEv(const AxisLine *self) {
  return self->lineWidth();
}

//  void AxisLine::setLineWidth(qreal newLineWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine12setLineWidthEd(AxisLine *self, qreal newLineWidth) {
  self->setLineWidth(newLineWidth);
}

//  bool AxisLine::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8AxisLine12isHorizontalEv(const AxisLine *self) {
  return self->isHorizontal();
}

//  void AxisLine::setIsHorizontal(bool newIsHorizontal)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine15setIsHorizontalEb(
    AxisLine *self,
    bool newIsHorizontal) {
  self->setIsHorizontal(newIsHorizontal);
}

//  void AxisLine::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine17componentCompleteEv(AxisLine *self) {
  self->componentComplete();
}

//  void AxisLine::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine14geometryChangeERK6QRectFS2_(
    AxisLine *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void AxisLine::iResolutionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine18iResolutionChangedEv(AxisLine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisLine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "iResolutionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "iResolutionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisLine::smoothingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine16smoothingChangedEv(AxisLine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisLine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "smoothingChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "smoothingChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisLine::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine12colorChangedEv(AxisLine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisLine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "colorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "colorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisLine::lineWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine16lineWidthChangedEv(AxisLine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisLine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "lineWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "lineWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void AxisLine::isHorizontalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisLine19isHorizontalChangedEv(AxisLine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "AxisLine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "isHorizontalChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "isHorizontalChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteAxisLine, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisLine(AxisLine *self, const char *key, void *call) {
  return static_cast<CuteAxisLine *>(self)->take(key, call);
}

//  void AxisLine::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8AxisLine17componentCompleteEv(AxisLine *self) {
  static_cast<OwnAxisLine *>(self)->OwnAxisLine::componentComplete();
}

//  void AxisLine::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8AxisLine14geometryChangeERK6QRectFS2_(
    AxisLine *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnAxisLine *>(self)->OwnAxisLine::geometryChange(
      *newGeometry,
      *oldGeometry);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom)))
