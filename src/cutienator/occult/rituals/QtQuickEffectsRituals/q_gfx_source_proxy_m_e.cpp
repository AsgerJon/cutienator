//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickEffects/6.12.0/QtQuickEffects/private/qgfxsourceproxy_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QGfxSourceProxyME' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 9 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#include <QtQuickEffects/QtQuickEffects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qgfxsourceproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickEffects/private/qgfxsourceproxy_p.h>
#include <QtQuick/private/qquickshadereffectsource_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuickEffects__QGfxSourceProxyME.cpp, line 1, as moc:QGfxSourceProxyME
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN17QGfxSourceProxyMEE_t {};
} // unnamed namespace

template <> constexpr inline auto QGfxSourceProxyME::qt_create_metaobjectdata<qt_meta_tag_ZN17QGfxSourceProxyMEE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QGfxSourceProxyME",
        "inputChanged",
        "",
        "outputChanged",
        "sourceRectChanged",
        "activeChanged",
        "interpolationChanged",
        "repolish",
        "input",
        "QQuickItem*",
        "output",
        "sourceRect",
        "QRectF",
        "active",
        "interpolation",
        "Interpolation",
        "Any",
        "Nearest",
        "Linear"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'inputChanged'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'outputChanged'
        QtMocHelpers::SignalData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'sourceRectChanged'
        QtMocHelpers::SignalData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'activeChanged'
        QtMocHelpers::SignalData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'interpolationChanged'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'repolish'
        QtMocHelpers::SlotData<void()>(7, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'input'
        QtMocHelpers::PropertyData<QQuickItem*>(8, 0x80000000 | 9, QMC::DefaultPropertyFlags | QMC::Writable | QMC::Resettable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 0),
        // property 'output'
        QtMocHelpers::PropertyData<QQuickItem*>(10, 0x80000000 | 9, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Final, 1),
        // property 'sourceRect'
        QtMocHelpers::PropertyData<QRectF>(11, 0x80000000 | 12, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 2),
        // property 'active'
        QtMocHelpers::PropertyData<bool>(13, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Final, 3),
        // property 'interpolation'
        QtMocHelpers::PropertyData<enum Interpolation>(14, 0x80000000 | 15, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 4),
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'Interpolation'
        QtMocHelpers::EnumData<enum Interpolation>(15, 15, QMC::EnumIsScoped).add({
            {   16, Interpolation::Any },
            {   17, Interpolation::Nearest },
            {   18, Interpolation::Linear },
        }),
    };
    return QtMocHelpers::metaObjectData<QGfxSourceProxyME, qt_meta_tag_ZN17QGfxSourceProxyMEE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QGfxSourceProxyME::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QGfxSourceProxyMEE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QGfxSourceProxyMEE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN17QGfxSourceProxyMEE_t>.metaTypes,
    nullptr
} };

void QGfxSourceProxyME::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QGfxSourceProxyME *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->inputChanged(); break;
        case 1: _t->outputChanged(); break;
        case 2: _t->sourceRectChanged(); break;
        case 3: _t->activeChanged(); break;
        case 4: _t->interpolationChanged(); break;
        case 5: _t->repolish(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QGfxSourceProxyME::*)()>(_a, &QGfxSourceProxyME::inputChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QGfxSourceProxyME::*)()>(_a, &QGfxSourceProxyME::outputChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QGfxSourceProxyME::*)()>(_a, &QGfxSourceProxyME::sourceRectChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QGfxSourceProxyME::*)()>(_a, &QGfxSourceProxyME::activeChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QGfxSourceProxyME::*)()>(_a, &QGfxSourceProxyME::interpolationChanged, 4))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 1:
        case 0:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QQuickItem* >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQuickItem**>(_v) = _t->input(); break;
        case 1: *reinterpret_cast<QQuickItem**>(_v) = _t->output(); break;
        case 2: *reinterpret_cast<QRectF*>(_v) = _t->sourceRect(); break;
        case 3: *reinterpret_cast<bool*>(_v) = _t->isActive(); break;
        case 4: *reinterpret_cast<enum Interpolation*>(_v) = _t->interpolation(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setInput(*reinterpret_cast<QQuickItem**>(_v)); break;
        case 2: _t->setSourceRect(*reinterpret_cast<QRectF*>(_v)); break;
        case 4: _t->setInterpolation(*reinterpret_cast<enum Interpolation*>(_v)); break;
        default: break;
        }
    }
    if (_c == QMetaObject::ResetProperty) {
        switch (_id) {
        case 0: _t->resetInput(); break;
        default: break;
        }
    }
}

const QMetaObject *QGfxSourceProxyME::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QGfxSourceProxyME::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QGfxSourceProxyMEE_t>.strings))
        return static_cast<void*>(this);
    return QQuickItem::qt_metacast(_clname);
}

int QGfxSourceProxyME::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 6;
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
void QGfxSourceProxyME::inputChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QGfxSourceProxyME::outputChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QGfxSourceProxyME::sourceRectChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QGfxSourceProxyME::activeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QGfxSourceProxyME::interpolationChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 97, as _ZN17QGfxSourceProxyME12updatePolishEv
inline void QGfxSourceProxyME::updatePolish()
{
    if (!m_input) {
        setOutput(nullptr);
        return;
    }

    QQuickImage *image = qobject_cast<QQuickImage *>(m_input);
    QQuickShaderEffectSource *shaderSource = qobject_cast<QQuickShaderEffectSource *>(m_input);
    bool childless = m_input->childItems().size() == 0;
    bool interpOk = m_interpolation == Interpolation::Any
                    || (m_interpolation == Interpolation::Linear && m_input->smooth() == true)
                    || (m_interpolation == Interpolation::Nearest && m_input->smooth() == false);

    // Layers can be used in two different ways. Option 1 is when the item is
    // used as input to a separate ShaderEffect component. In this case,
    // m_input will be the item itself.
    QObject *layer = findLayer(m_input);
    if (!layer && shaderSource) {
        // Alternatively, the effect is applied via layer.effect, and the
        // input to the effect will be the layer's internal ShaderEffectSource
        // item. In this case, we need to backtrack and find the item that has
        // the layer and configure it accordingly.
        layer = findLayer(shaderSource->sourceItem());
    }

    // A bit crude test, but we're only using source rect for
    // blurring+transparent edge, so this is good enough.
    bool padded = m_sourceRect.x() < 0 || m_sourceRect.y() < 0;

    bool direct = false;

    if (layer) {
        // Auto-configure the layer so interpolation and padding works as
        // expected without allocating additional FBOs. In edgecases, where
        // this feature is undesiered, the user can simply use
        // ShaderEffectSource rather than layer.
        layer->setProperty("sourceRect", m_sourceRect);
        layer->setProperty("smooth", m_interpolation != Interpolation::Nearest);
        direct = true;

    } else if (childless && interpOk) {
        if (shaderSource) {
            if (shaderSource->sourceRect() == m_sourceRect || m_sourceRect.isEmpty())
                direct = true;

        } else if (!padded && ((image && image->fillMode() == QQuickImage::Stretch && !image->sourceSize().isNull())
                                || (!image && m_input->isTextureProvider())
                              )
                  ) {
            direct = true;
        }
    }

    if (direct)
        setOutput(m_input);
    else
        useProxy();

    // Remove the proxy if it is not in use..
    if (m_proxy && m_output == m_input) {
        delete m_proxy;
        m_proxy = nullptr;
    }
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 79, as _ZN17QGfxSourceProxyME8repolishEv
inline void QGfxSourceProxyME::repolish()
{
    polish();
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 13, as _ZN17QGfxSourceProxyMEC1EP10QQuickItem
inline QGfxSourceProxyME::QGfxSourceProxyME(QQuickItem *parentItem)
    : QQuickItem(parentItem)
{
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 18, as _ZN17QGfxSourceProxyMED1Ev
inline QGfxSourceProxyME::~QGfxSourceProxyME()
{
    delete m_proxy;
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 23, as _ZN17QGfxSourceProxyME8setInputEP10QQuickItem
inline void QGfxSourceProxyME::setInput(QQuickItem *input)
{
    if (m_input == input)
        return;

    if (m_input)
        disconnect(m_input, nullptr, this, nullptr);
    m_input = input;
    polish();
    if (m_input) {
        if (QQuickImage *image = qobject_cast<QQuickImage *>(m_input)) {
            connect(image, &QQuickImage::sourceSizeChanged, this, &QGfxSourceProxyME::repolish);
            connect(image, &QQuickImage::fillModeChanged, this, &QGfxSourceProxyME::repolish);
        }
        connect(m_input, &QQuickItem::childrenChanged, this, &QGfxSourceProxyME::repolish);
    }
    Q_EMIT inputChanged();
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 51, as _ZN17QGfxSourceProxyME13setSourceRectERK6QRectF
inline void QGfxSourceProxyME::setSourceRect(const QRectF &sourceRect)
{
    if (m_sourceRect == sourceRect)
        return;
    m_sourceRect = sourceRect;
    polish();
    Q_EMIT sourceRectChanged();
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 60, as _ZN17QGfxSourceProxyME16setInterpolationENS_13InterpolationE
inline void QGfxSourceProxyME::setInterpolation(Interpolation i)
{
    if (m_interpolation == i)
        return;
    m_interpolation = i;
    polish();
    Q_EMIT interpolationChanged();
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 42, as _ZN17QGfxSourceProxyME9setOutputEP10QQuickItem
inline void QGfxSourceProxyME::setOutput(QQuickItem *output)
{
    if (m_output == output)
        return;
    m_output = output;
    Q_EMIT activeChanged();
    Q_EMIT outputChanged();
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 69, as _ZN17QGfxSourceProxyME8useProxyEv
inline void QGfxSourceProxyME::useProxy()
{
    if (!m_proxy)
        m_proxy = new QQuickShaderEffectSource(this);
    m_proxy->setSourceRect(m_sourceRect);
    m_proxy->setSourceItem(m_input);
    m_proxy->setSmooth(m_interpolation != Interpolation::Nearest);
    setOutput(m_proxy);
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 84, as _ZN17QGfxSourceProxyME9findLayerEP10QQuickItem
inline QObject *QGfxSourceProxyME::findLayer(QQuickItem *item)
{
    if (!item)
        return nullptr;
    QQuickItemPrivate *d = QQuickItemPrivate::get(item);
    if (d->extra.isAllocated() && d->extra->layer) {
        QObject *layer = qvariant_cast<QObject *>(item->property("layer"));
        if (layer && layer->property("enabled").toBool())
            return layer;
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  Only a class built on QGfxSourceProxyME may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGfxSourceProxyME : QGfxSourceProxyME {
  using QGfxSourceProxyME::updatePolish;
};

//  A QGfxSourceProxyME that Python can take functions over in. Every QGfxSourceProxyME
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGfxSourceProxyMECall0)(const void *, int *);
typedef const QRectF * (*CuteQGfxSourceProxyMECall1)(const void *, int *);
typedef const QRectF * (*CuteQGfxSourceProxyMECall2)(const void *, int *);
typedef bool (*CuteQGfxSourceProxyMECall3)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQGfxSourceProxyMECall4)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQGfxSourceProxyMECall5)(const void *, int *);
typedef void * (*CuteQGfxSourceProxyMECall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGfxSourceProxyMECall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQGfxSourceProxyMECall8)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQGfxSourceProxyMECall9)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQGfxSourceProxyMECall10)(const void *, int *);
typedef void (*CuteQGfxSourceProxyMECall11)(const void *, int *);
typedef void (*CuteQGfxSourceProxyMECall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQGfxSourceProxyMECall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQGfxSourceProxyMECall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall21)(const void *, int *);
typedef void (*CuteQGfxSourceProxyMECall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQGfxSourceProxyMECall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQGfxSourceProxyMECall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQGfxSourceProxyMECall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGfxSourceProxyMECall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGfxSourceProxyMECall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGfxSourceProxyMECall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGfxSourceProxyMECall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQGfxSourceProxyMECall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQGfxSourceProxyMECall33)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQGfxSourceProxyMECall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGfxSourceProxyMECall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGfxSourceProxyMECall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGfxSourceProxyMECall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGfxSourceProxyMECall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGfxSourceProxyMECall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGfxSourceProxyMECall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGfxSourceProxyME : public QGfxSourceProxyME {
public:
  using QGfxSourceProxyME::QGfxSourceProxyME;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
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

  //  void QGfxSourceProxyME::updatePolish()
  void updatePolish() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall0 call = reinterpret_cast<CuteQGfxSourceProxyMECall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGfxSourceProxyME::updatePolish();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall1 call = reinterpret_cast<CuteQGfxSourceProxyMECall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall2 call = reinterpret_cast<CuteQGfxSourceProxyMECall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall3 call = reinterpret_cast<CuteQGfxSourceProxyMECall3>(taken[3]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall4 call = reinterpret_cast<CuteQGfxSourceProxyMECall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall5 call = reinterpret_cast<CuteQGfxSourceProxyMECall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall6 call = reinterpret_cast<CuteQGfxSourceProxyMECall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall7 call = reinterpret_cast<CuteQGfxSourceProxyMECall7>(taken[7]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall8 call = reinterpret_cast<CuteQGfxSourceProxyMECall8>(taken[8]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall9 call = reinterpret_cast<CuteQGfxSourceProxyMECall9>(taken[9]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall10 call = reinterpret_cast<CuteQGfxSourceProxyMECall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall11 call = reinterpret_cast<CuteQGfxSourceProxyMECall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall12 call = reinterpret_cast<CuteQGfxSourceProxyMECall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall13 call = reinterpret_cast<CuteQGfxSourceProxyMECall13>(taken[13]);
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
      CuteQGfxSourceProxyMECall14 call = reinterpret_cast<CuteQGfxSourceProxyMECall14>(taken[14]);
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
      CuteQGfxSourceProxyMECall15 call = reinterpret_cast<CuteQGfxSourceProxyMECall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall16 call = reinterpret_cast<CuteQGfxSourceProxyMECall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall17 call = reinterpret_cast<CuteQGfxSourceProxyMECall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall18 call = reinterpret_cast<CuteQGfxSourceProxyMECall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall19 call = reinterpret_cast<CuteQGfxSourceProxyMECall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall20 call = reinterpret_cast<CuteQGfxSourceProxyMECall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall21 call = reinterpret_cast<CuteQGfxSourceProxyMECall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall22 call = reinterpret_cast<CuteQGfxSourceProxyMECall22>(taken[22]);
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
      CuteQGfxSourceProxyMECall23 call = reinterpret_cast<CuteQGfxSourceProxyMECall23>(taken[23]);
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
      CuteQGfxSourceProxyMECall24 call = reinterpret_cast<CuteQGfxSourceProxyMECall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall25 call = reinterpret_cast<CuteQGfxSourceProxyMECall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall26 call = reinterpret_cast<CuteQGfxSourceProxyMECall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall27 call = reinterpret_cast<CuteQGfxSourceProxyMECall27>(taken[27]);
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
      CuteQGfxSourceProxyMECall28 call = reinterpret_cast<CuteQGfxSourceProxyMECall28>(taken[28]);
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
      CuteQGfxSourceProxyMECall29 call = reinterpret_cast<CuteQGfxSourceProxyMECall29>(taken[29]);
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
      CuteQGfxSourceProxyMECall30 call = reinterpret_cast<CuteQGfxSourceProxyMECall30>(taken[30]);
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
      CuteQGfxSourceProxyMECall31 call = reinterpret_cast<CuteQGfxSourceProxyMECall31>(taken[31]);
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
      CuteQGfxSourceProxyMECall32 call = reinterpret_cast<CuteQGfxSourceProxyMECall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall33 call = reinterpret_cast<CuteQGfxSourceProxyMECall33>(taken[33]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall34 call = reinterpret_cast<CuteQGfxSourceProxyMECall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQGfxSourceProxyMECall35 call = reinterpret_cast<CuteQGfxSourceProxyMECall35>(taken[35]);
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
      CuteQGfxSourceProxyMECall36 call = reinterpret_cast<CuteQGfxSourceProxyMECall36>(taken[36]);
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
      CuteQGfxSourceProxyMECall37 call = reinterpret_cast<CuteQGfxSourceProxyMECall37>(taken[37]);
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
      CuteQGfxSourceProxyMECall38 call = reinterpret_cast<CuteQGfxSourceProxyMECall38>(taken[38]);
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
      CuteQGfxSourceProxyMECall39 call = reinterpret_cast<CuteQGfxSourceProxyMECall39>(taken[39]);
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
      CuteQGfxSourceProxyMECall40 call = reinterpret_cast<CuteQGfxSourceProxyMECall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGfxSourceProxyME::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGfxSourceProxyME10metaObjectEv(
    const QGfxSourceProxyME *self) {
  return self->metaObject();
}

//  void *QGfxSourceProxyME::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QGfxSourceProxyME11qt_metacastEPKc(
    QGfxSourceProxyME *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGfxSourceProxyME::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QGfxSourceProxyME11qt_metacallEN11QMetaObject4CallEiPPv(
    QGfxSourceProxyME *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGfxSourceProxyME::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGfxSourceProxyME2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGfxSourceProxyME::tr(s, c, n));
}

//  QGfxSourceProxyME::QGfxSourceProxyME(QQuickItem *parentItem)
extern "C" Q_DECL_EXPORT
QGfxSourceProxyME *ritual_ZN17QGfxSourceProxyMEC1EP10QQuickItem(
    QQuickItem *parentItem) {
  return new CuteQGfxSourceProxyME(parentItem);
}

//  QGfxSourceProxyME::~QGfxSourceProxyME()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyMED1Ev(QGfxSourceProxyME *self) {
  delete self;
}

//  QQuickItem *QGfxSourceProxyME::input() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QGfxSourceProxyME5inputEv(
    const QGfxSourceProxyME *self) {
  return self->input();
}

//  void QGfxSourceProxyME::setInput(QQuickItem *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME8setInputEP10QQuickItem(
    QGfxSourceProxyME *self,
    QQuickItem *input) {
  self->setInput(input);
}

//  void QGfxSourceProxyME::resetInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME10resetInputEv(QGfxSourceProxyME *self) {
  self->resetInput();
}

//  QQuickItem *QGfxSourceProxyME::output() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QGfxSourceProxyME6outputEv(
    const QGfxSourceProxyME *self) {
  return self->output();
}

//  QRectF QGfxSourceProxyME::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGfxSourceProxyME10sourceRectEv(
    const QGfxSourceProxyME *self) {
  return new QRectF(self->sourceRect());
}

//  void QGfxSourceProxyME::setSourceRect(const QRectF &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME13setSourceRectERK6QRectF(
    QGfxSourceProxyME *self,
    const QRectF *sourceRect) {
  self->setSourceRect(*sourceRect);
}

//  bool QGfxSourceProxyME::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGfxSourceProxyME8isActiveEv(
    const QGfxSourceProxyME *self) {
  return self->isActive();
}

//  void QGfxSourceProxyME::setInterpolation(Interpolation i)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME16setInterpolationENS_13InterpolationE(
    QGfxSourceProxyME *self,
    QGfxSourceProxyME::Interpolation i) {
  self->setInterpolation(i);
}

//  Interpolation QGfxSourceProxyME::interpolation() const
extern "C" Q_DECL_EXPORT
QGfxSourceProxyME::Interpolation ritual_ZNK17QGfxSourceProxyME13interpolationEv(
    const QGfxSourceProxyME *self) {
  return self->interpolation();
}

//  void QGfxSourceProxyME::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME12updatePolishEv(QGfxSourceProxyME *self) {
  self->updatePolish();
}

//  void QGfxSourceProxyME::inputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME12inputChangedEv(QGfxSourceProxyME *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGfxSourceProxyME")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "inputChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "inputChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGfxSourceProxyME::outputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME13outputChangedEv(QGfxSourceProxyME *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGfxSourceProxyME")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "outputChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "outputChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGfxSourceProxyME::sourceRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME17sourceRectChangedEv(
    QGfxSourceProxyME *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGfxSourceProxyME")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sourceRectChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sourceRectChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGfxSourceProxyME::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME13activeChangedEv(QGfxSourceProxyME *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGfxSourceProxyME")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGfxSourceProxyME::interpolationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME20interpolationChangedEv(
    QGfxSourceProxyME *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGfxSourceProxyME")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "interpolationChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "interpolationChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGfxSourceProxyME::repolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME8repolishEv(QGfxSourceProxyME *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGfxSourceProxyME")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "repolish()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "repolish()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGfxSourceProxyME::setOutput(QQuickItem *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME9setOutputEP10QQuickItem(
    QGfxSourceProxyME *self,
    QQuickItem *output) {
  self->setOutput(output);
}

//  void QGfxSourceProxyME::useProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGfxSourceProxyME8useProxyEv(QGfxSourceProxyME *self) {
  self->useProxy();
}

//  QObject *QGfxSourceProxyME::findLayer(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QGfxSourceProxyME9findLayerEP10QQuickItem(
    QQuickItem *a0) {
  return QGfxSourceProxyME::findLayer(a0);
}

//  a Python function taken by a CuteQGfxSourceProxyME, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGfxSourceProxyME(
    QGfxSourceProxyME *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGfxSourceProxyME *>(self)->take(key, call);
}

//  void QGfxSourceProxyME::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGfxSourceProxyME12updatePolishEv(
    QGfxSourceProxyME *self) {
  static_cast<OwnQGfxSourceProxyME *>(self)->OwnQGfxSourceProxyME::updatePolish();
}
