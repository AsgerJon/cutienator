//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQStyleKitDelegate' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 6 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsStyleKit/private/qqstylekitdelegate_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#include <QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/private/qquickimplicitsizeitem_p_p.h>
#include <QtQuickControls2Impl/private/qquickcolorimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKit__QQStyleKitDelegate.cpp, line 1, as moc:QQStyleKitDelegate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QQStyleKitDelegateE_t {};
} // unnamed namespace

template <> constexpr inline auto QQStyleKitDelegate::qt_create_metaobjectdata<qt_meta_tag_ZN18QQStyleKitDelegateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQStyleKitDelegate",
        "QML.Element",
        "StyledItem",
        "delegateStyleChanged",
        "",
        "delegateStyle",
        "QQStyleKitDelegateProperties*"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'delegateStyleChanged'
        QtMocHelpers::SignalData<void()>(3, 4, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'delegateStyle'
        QtMocHelpers::PropertyData<QQStyleKitDelegateProperties*>(5, 0x80000000 | 6, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final | QMC::Required, 0),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQStyleKitDelegate, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQStyleKitDelegate::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickImplicitSizeItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQStyleKitDelegateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQStyleKitDelegateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QQStyleKitDelegateE_t>.metaTypes,
    nullptr
} };

void QQStyleKitDelegate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQStyleKitDelegate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->delegateStyleChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitDelegate::*)()>(_a, &QQStyleKitDelegate::delegateStyleChanged, 0))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQStyleKitDelegateProperties**>(_v) = _t->delegateStyle(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setDelegateStyle(*reinterpret_cast<QQStyleKitDelegateProperties**>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQStyleKitDelegate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQStyleKitDelegate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QQStyleKitDelegateE_t>.strings))
        return static_cast<void*>(this);
    return QQuickImplicitSizeItem::qt_metacast(_clname);
}

int QQStyleKitDelegate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickImplicitSizeItem::qt_metacall(_c, _id, _a);
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
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}

// SIGNAL 0
void QQStyleKitDelegate::delegateStyleChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 67, as _ZN18QQStyleKitDelegateC1EP10QQuickItem
inline QQStyleKitDelegate::QQStyleKitDelegate(QQuickItem *parent)
    : QQuickImplicitSizeItem(*new QQuickImplicitSizeItemPrivate, parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 72, as _ZNK18QQStyleKitDelegate13delegateStyleEv
inline QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle() const
{
    return m_delegateProperties;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 77, as _ZN18QQStyleKitDelegate16setDelegateStyleEP28QQStyleKitDelegateProperties
inline void QQStyleKitDelegate::setDelegateStyle(QQStyleKitDelegateProperties *delegateStyle)
{
    if (m_delegateProperties == delegateStyle)
        return;

    if (m_delegateProperties)
        disconnect(m_delegateProperties, nullptr, this, nullptr);

    m_delegateProperties = delegateStyle;

    if (!qmlEngine(this)) {
        qmlWarning(this) << "Unable to draw delegate: no QQmlEngine found";
        return;
    }

    maybeCreateColor();
    maybeCreateGradient();
    maybeCreateImage();
    updateImplicitSize();

    connect(m_delegateProperties, &QQStyleKitDelegateProperties::widthChanged, this, &QQStyleKitDelegate::updateImplicitSize);
    connect(m_delegateProperties, &QQStyleKitDelegateProperties::heightChanged, this, &QQStyleKitDelegate::updateImplicitSize);

    emit delegateStyleChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 103, as _ZN18QQStyleKitDelegate18updateImplicitSizeEv
inline void QQStyleKitDelegate::updateImplicitSize()
{
    if (!m_delegateProperties)
        return;

    /* The implicit size of this item is determined by the following priority:
     * 1. The width/height set on DelegateStyle (clamped to minimumWidth/minimumHeight)
     * 2. The implicit size of the image overlay (if present)
     * 3. Zero */
    const qreal widthInStyle = qMax(m_delegateProperties->minimumWidth(), m_delegateProperties->width());
    const qreal heightInStyle = qMax(m_delegateProperties->minimumHeight(), m_delegateProperties->height());
    setImplicitWidth(widthInStyle > 0 || !m_imageOverlay ? widthInStyle : m_imageOverlay->implicitWidth());
    setImplicitHeight(heightInStyle > 0 || !m_imageOverlay ? heightInStyle : m_imageOverlay->implicitHeight());
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 118, as _ZN18QQStyleKitDelegate16maybeCreateColorEv
inline void QQStyleKitDelegate::maybeCreateColor()
{
    if (m_colorOverlay)
        return;
    if (!m_delegateProperties)
        return;
    if (m_delegateProperties->color().alpha() == 0
        && (m_delegateProperties->border()->color().alpha() == 0
            || m_delegateProperties->border()->width() == 0)) {
        // Lazy-create the color rectangle later, if/when needed
        connect(m_delegateProperties, &QQStyleKitDelegateProperties::colorChanged,
                this, &QQStyleKitDelegate::maybeCreateColor, Qt::UniqueConnection);
        connect(m_delegateProperties->border(), &QQStyleKitBorderProperties::colorChanged,
                this, &QQStyleKitDelegate::maybeCreateColor, Qt::UniqueConnection);
        connect(m_delegateProperties->border(), &QQStyleKitBorderProperties::widthChanged,
                this, &QQStyleKitDelegate::maybeCreateColor, Qt::UniqueConnection);
        return;
    }

    disconnect(m_delegateProperties, &QQStyleKitDelegateProperties::colorChanged,
            this, &QQStyleKitDelegate::maybeCreateColor);
    disconnect(m_delegateProperties->border(), &QQStyleKitBorderProperties::colorChanged,
            this, &QQStyleKitDelegate::maybeCreateColor);
    disconnect(m_delegateProperties->border(), &QQStyleKitBorderProperties::widthChanged,
            this, &QQStyleKitDelegate::maybeCreateColor);

    QQmlEngine *engine = qmlEngine(this);
    Q_ASSERT(engine);
    static QQmlComponent *component = nullptr;
    if (!component || component->engine() != engine) {
        delete component;
        component = new QQmlComponent(engine);
        const auto qmlCode = R"(
            import QtQuick
            Rectangle {
                z: -3
                width: parent.width
                height: parent.height
                color: delegateStyle.color
                opacity: delegateStyle.opacity
                topLeftRadius: delegateStyle.topLeftRadius
                topRightRadius: delegateStyle.topRightRadius
                bottomLeftRadius: delegateStyle.bottomLeftRadius
                bottomRightRadius: delegateStyle.bottomRightRadius
                border.width: delegateStyle.border.width
                border.color: delegateStyle.border.color
            }
        )"_ba;
        component->setData(qmlCode, QUrl());
        Q_ASSERT_X(!component->isError(), __FUNCTION__, component->errorString().toUtf8().constData());
    }

    QQmlContext *ctx = QQmlEngine::contextForObject(this);
    m_colorOverlay = qobject_cast<QQuickItem*>(component->beginCreate(ctx));
    Q_ASSERT(m_colorOverlay);
    m_colorOverlay->setParent(this);
    m_colorOverlay->setParentItem(this);
    component->completeCreate();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 178, as _ZN18QQStyleKitDelegate19maybeCreateGradientEv
inline void QQStyleKitDelegate::maybeCreateGradient()
{
    /* Unlike a Rectangle, a StyledItem draws both the color and the gradient at
     * the same time. This allows a style to define them independently. That way you can
     * define a common semi-transparent grayscale gradient once for a delegate in the style
     * (e.g for control.background.gradient), and then tint it with different colors for
     * different controls, states, or themes (e.g for button.hovered.background.color). */
    if (m_gradientOverlay)
        return;
    if (!m_delegateProperties)
        return;
    if (!m_delegateProperties->gradient()) {
        connect(m_delegateProperties, &QQStyleKitDelegateProperties::gradientChanged,
                this, &QQStyleKitDelegate::maybeCreateGradient, Qt::UniqueConnection);
        return;
    }

    disconnect(m_delegateProperties, &QQStyleKitDelegateProperties::gradientChanged,
               this, &QQStyleKitDelegate::maybeCreateGradient);

    QQmlEngine *engine = qmlEngine(this);
    Q_ASSERT(engine);
    static QQmlComponent *component = nullptr;
    if (!component || component->engine() != engine) {
        delete component;
        component = new QQmlComponent(engine);
        const auto qmlCode = R"(
            import QtQuick
            Rectangle {
                z: -2
                width: parent.width
                height: parent.height
                color: "transparent"
                visible: delegateStyle.gradient != null
                gradient: delegateStyle.gradient
                topLeftRadius: delegateStyle.topLeftRadius
                topRightRadius: delegateStyle.topRightRadius
                bottomLeftRadius: delegateStyle.bottomLeftRadius
                bottomRightRadius: delegateStyle.bottomRightRadius
                border.width: delegateStyle.border.width
                border.color: delegateStyle.border.color
            }
        )"_ba;
        component->setData(qmlCode, QUrl());
        Q_ASSERT_X(!component->isError(), __FUNCTION__, component->errorString().toUtf8().constData());
    }

    QQmlContext *ctx = QQmlEngine::contextForObject(this);
    m_gradientOverlay = qobject_cast<QQuickItem*>(component->beginCreate(ctx));
    Q_ASSERT(m_gradientOverlay);
    m_gradientOverlay->setParent(this);
    m_gradientOverlay->setParentItem(this);
    component->completeCreate();
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 233, as _ZN18QQStyleKitDelegate16maybeCreateImageEv
inline void QQStyleKitDelegate::maybeCreateImage()
{
    if (m_imageOverlay)
        return;
    if (!m_delegateProperties)
        return;
    if (m_delegateProperties->image()->source().isEmpty()
        || m_delegateProperties->image()->color().alpha() == 0) {
        connect(m_delegateProperties->image(), &QQStyleKitImageProperties::sourceChanged,
                this, &QQStyleKitDelegate::maybeCreateImage, Qt::UniqueConnection);
        connect(m_delegateProperties->image(), &QQStyleKitImageProperties::colorChanged,
                this, &QQStyleKitDelegate::maybeCreateImage, Qt::UniqueConnection);
        return;
    }

    disconnect(m_delegateProperties->image(), &QQStyleKitImageProperties::sourceChanged,
               this, &QQStyleKitDelegate::maybeCreateImage);
    disconnect(m_delegateProperties->image(), &QQStyleKitImageProperties::colorChanged,
               this, &QQStyleKitDelegate::maybeCreateImage);

    QQmlEngine *engine = qmlEngine(this);
    Q_ASSERT(engine);
    static QQmlComponent *component = nullptr;
    if (!component || component->engine() != engine) {
        delete component;
        component = new QQmlComponent(engine);
        const auto qmlCode = R"(
            import QtQuick.Controls.impl
            ColorImage {
                z: -1
                width: parent.width
                height: parent.height
                color: delegateStyle.image.color
                source: delegateStyle.image.source
                fillMode: delegateStyle.image.fillMode
            }
        )"_ba;
        component->setData(qmlCode, QUrl());
        Q_ASSERT_X(!component->isError(), __FUNCTION__, component->errorString().toUtf8().constData());
    }

    QQmlContext *ctx = QQmlEngine::contextForObject(this);
    m_imageOverlay = qobject_cast<QQuickItem*>(component->beginCreate(ctx));
    m_imageOverlay->setParent(this);
    m_imageOverlay->setParentItem(this);
    component->completeCreate();

    updateImplicitSize();
    connect(m_imageOverlay, &QQuickItem::implicitWidthChanged, this, &QQStyleKitDelegate::updateImplicitSize);
    connect(m_imageOverlay, &QQuickItem::implicitHeightChanged, this, &QQStyleKitDelegate::updateImplicitSize);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQStyleKitDelegate10metaObjectEv(
    const QQStyleKitDelegate *self) {
  return self->metaObject();
}

//  void *QQStyleKitDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQStyleKitDelegate11qt_metacastEPKc(
    QQStyleKitDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQStyleKitDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQStyleKitDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitDelegate::tr(s, c, n));
}

//  QQStyleKitDelegate::QQStyleKitDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitDelegate *ritual_ZN18QQStyleKitDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQStyleKitDelegate(parent);
}

//  QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle() const
extern "C" Q_DECL_EXPORT
QQStyleKitDelegateProperties *ritual_ZNK18QQStyleKitDelegate13delegateStyleEv(
    const QQStyleKitDelegate *self) {
  return self->delegateStyle();
}

//  void QQStyleKitDelegate::setDelegateStyle(QQStyleKitDelegateProperties
//      *delegateStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate16setDelegateStyleEP28QQStyleKitDelegateProperties(
    QQStyleKitDelegate *self,
    QQStyleKitDelegateProperties *delegateStyle) {
  self->setDelegateStyle(delegateStyle);
}

//  void QQStyleKitDelegate::delegateStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate20delegateStyleChangedEv(
    QQStyleKitDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "delegateStyleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "delegateStyleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitDelegate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate18updateImplicitSizeEv(
    QQStyleKitDelegate *self) {
  self->updateImplicitSize();
}

//  void QQStyleKitDelegate::maybeCreateColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate16maybeCreateColorEv(
    QQStyleKitDelegate *self) {
  self->maybeCreateColor();
}

//  void QQStyleKitDelegate::maybeCreateGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate19maybeCreateGradientEv(
    QQStyleKitDelegate *self) {
  self->maybeCreateGradient();
}

//  void QQStyleKitDelegate::maybeCreateImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate16maybeCreateImageEv(
    QQStyleKitDelegate *self) {
  self->maybeCreateImage();
}
