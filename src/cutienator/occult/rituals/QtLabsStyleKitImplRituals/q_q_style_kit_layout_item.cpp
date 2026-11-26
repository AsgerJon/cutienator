//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  Impl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQStyleKitLayoutItem' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 11 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsStyleKitImpl/QtLabsStyleKitImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtLabsStyleKitImpl__QQStyleKitLayoutItem.cpp, line 1, as moc:QQStyleKitLayoutItem
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN20QQStyleKitLayoutItemE_t {};
} // unnamed namespace

template <> constexpr inline auto QQStyleKitLayoutItem::qt_create_metaobjectdata<qt_meta_tag_ZN20QQStyleKitLayoutItemE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQStyleKitLayoutItem",
        "QML.Element",
        "StyleKitLayoutItem",
        "itemChanged",
        "",
        "xChanged",
        "yChanged",
        "widthChanged",
        "heightChanged",
        "alignmentChanged",
        "marginsChanged",
        "fillWidthChanged",
        "fillHeightChanged",
        "item",
        "QQuickItem*",
        "x",
        "y",
        "width",
        "height",
        "alignment",
        "Qt::Alignment",
        "margins",
        "QMarginsF",
        "fillWidth",
        "fillHeight"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'itemChanged'
        QtMocHelpers::SignalData<void()>(3, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'xChanged'
        QtMocHelpers::SignalData<void()>(5, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'yChanged'
        QtMocHelpers::SignalData<void()>(6, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'widthChanged'
        QtMocHelpers::SignalData<void()>(7, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'heightChanged'
        QtMocHelpers::SignalData<void()>(8, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'alignmentChanged'
        QtMocHelpers::SignalData<void()>(9, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'marginsChanged'
        QtMocHelpers::SignalData<void()>(10, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'fillWidthChanged'
        QtMocHelpers::SignalData<void()>(11, 4, QMC::AccessPublic, QMetaType::Void),
        // Signal 'fillHeightChanged'
        QtMocHelpers::SignalData<void()>(12, 4, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'item'
        QtMocHelpers::PropertyData<QQuickItem*>(13, 0x80000000 | 14, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 0),
        // property 'x'
        QtMocHelpers::PropertyData<qreal>(15, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Final, 1),
        // property 'y'
        QtMocHelpers::PropertyData<qreal>(16, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Final, 2),
        // property 'width'
        QtMocHelpers::PropertyData<qreal>(17, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Final, 3),
        // property 'height'
        QtMocHelpers::PropertyData<qreal>(18, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Final, 4),
        // property 'alignment'
        QtMocHelpers::PropertyData<Qt::Alignment>(19, 0x80000000 | 20, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 5),
        // property 'margins'
        QtMocHelpers::PropertyData<QMarginsF>(21, 0x80000000 | 22, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final, 6),
        // property 'fillWidth'
        QtMocHelpers::PropertyData<bool>(23, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 7),
        // property 'fillHeight'
        QtMocHelpers::PropertyData<bool>(24, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final, 8),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
    });
    return QtMocHelpers::metaObjectData<QQStyleKitLayoutItem, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQStyleKitLayoutItem::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQStyleKitLayoutItemE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQStyleKitLayoutItemE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN20QQStyleKitLayoutItemE_t>.metaTypes,
    nullptr
} };

void QQStyleKitLayoutItem::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQStyleKitLayoutItem *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->itemChanged(); break;
        case 1: _t->xChanged(); break;
        case 2: _t->yChanged(); break;
        case 3: _t->widthChanged(); break;
        case 4: _t->heightChanged(); break;
        case 5: _t->alignmentChanged(); break;
        case 6: _t->marginsChanged(); break;
        case 7: _t->fillWidthChanged(); break;
        case 8: _t->fillHeightChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::itemChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::xChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::yChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::widthChanged, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::heightChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::alignmentChanged, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::marginsChanged, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::fillWidthChanged, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQStyleKitLayoutItem::*)()>(_a, &QQStyleKitLayoutItem::fillHeightChanged, 8))
            return;
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 0:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QQuickItem* >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQuickItem**>(_v) = _t->item(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->x(); break;
        case 2: *reinterpret_cast<qreal*>(_v) = _t->y(); break;
        case 3: *reinterpret_cast<qreal*>(_v) = _t->width(); break;
        case 4: *reinterpret_cast<qreal*>(_v) = _t->height(); break;
        case 5: *reinterpret_cast<Qt::Alignment*>(_v) = _t->alignment(); break;
        case 6: *reinterpret_cast<QMarginsF*>(_v) = _t->margins(); break;
        case 7: *reinterpret_cast<bool*>(_v) = _t->fillWidth(); break;
        case 8: *reinterpret_cast<bool*>(_v) = _t->fillHeight(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setItem(*reinterpret_cast<QQuickItem**>(_v)); break;
        case 5: _t->setAlignment(*reinterpret_cast<Qt::Alignment*>(_v)); break;
        case 6: _t->setMargins(*reinterpret_cast<QMarginsF*>(_v)); break;
        case 7: _t->setFillWidth(*reinterpret_cast<bool*>(_v)); break;
        case 8: _t->setFillHeight(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQStyleKitLayoutItem::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQStyleKitLayoutItem::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN20QQStyleKitLayoutItemE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQStyleKitLayoutItem::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 9)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 9)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 9;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 9;
    }
    return _id;
}

// SIGNAL 0
void QQStyleKitLayoutItem::itemChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQStyleKitLayoutItem::xChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQStyleKitLayoutItem::yChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void QQStyleKitLayoutItem::widthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void QQStyleKitLayoutItem::heightChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 4, nullptr);
}

// SIGNAL 5
void QQStyleKitLayoutItem::alignmentChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void QQStyleKitLayoutItem::marginsChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 6, nullptr);
}

// SIGNAL 7
void QQStyleKitLayoutItem::fillWidthChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 7, nullptr);
}

// SIGNAL 8
void QQStyleKitLayoutItem::fillHeightChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 8, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 69, as _ZN20QQStyleKitLayoutItemC1EP7QObject
inline QQStyleKitLayoutItem::QQStyleKitLayoutItem(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 74, as _ZNK20QQStyleKitLayoutItem4itemEv
inline QQuickItem *QQStyleKitLayoutItem::item() const
{
    return m_item;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 79, as _ZN20QQStyleKitLayoutItem7setItemEP10QQuickItem
inline void QQStyleKitLayoutItem::setItem(QQuickItem *item)
{
    if (m_item == item)
        return;

    if (m_item)
        disconnect(m_item, nullptr, this, nullptr);

    m_item = item;
    if (m_item) {
        connect(m_item, &QQuickItem::implicitWidthChanged, this, [this]() { emit itemChanged(); });
        connect(m_item, &QQuickItem::implicitHeightChanged, this, [this]() { emit itemChanged(); });
        connect(m_item, &QQuickItem::visibleChanged, this, [this]() { emit itemChanged(); });
    }
    // TODO: parentchanged
    emit itemChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 97, as _ZNK20QQStyleKitLayoutItem1xEv
inline qreal QQStyleKitLayoutItem::x() const
{
    return m_x;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 102, as _ZN20QQStyleKitLayoutItem4setXEd
inline void QQStyleKitLayoutItem::setX(qreal x)
{
    if (qFuzzyCompare(m_x, x))
        return;

    m_x = x;
    emit xChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 111, as _ZNK20QQStyleKitLayoutItem1yEv
inline qreal QQStyleKitLayoutItem::y() const
{
    return m_y;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 116, as _ZN20QQStyleKitLayoutItem4setYEd
inline void QQStyleKitLayoutItem::setY(qreal y)
{
    if (qFuzzyCompare(m_y, y))
        return;

    m_y = y;
    emit yChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 125, as _ZNK20QQStyleKitLayoutItem5widthEv
inline qreal QQStyleKitLayoutItem::width() const
{
    return m_width;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 130, as _ZN20QQStyleKitLayoutItem8setWidthEd
inline void QQStyleKitLayoutItem::setWidth(qreal width)
{
    if (qFuzzyCompare(m_width, width))
        return;

    m_width = width;
    emit widthChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 139, as _ZNK20QQStyleKitLayoutItem6heightEv
inline qreal QQStyleKitLayoutItem::height() const
{
    return m_height;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 144, as _ZN20QQStyleKitLayoutItem9setHeightEd
inline void QQStyleKitLayoutItem::setHeight(qreal height)
{
    if (qFuzzyCompare(m_height, height))
        return;

    m_height = height;
    emit heightChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 153, as _ZNK20QQStyleKitLayoutItem9alignmentEv
inline Qt::Alignment QQStyleKitLayoutItem::alignment() const
{
    return m_alignment;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 158, as _ZN20QQStyleKitLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE
inline void QQStyleKitLayoutItem::setAlignment(Qt::Alignment alignment)
{
    if (m_alignment == alignment)
        return;

    m_alignment = alignment;
    emit alignmentChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 167, as _ZNK20QQStyleKitLayoutItem7marginsEv
inline QMarginsF QQStyleKitLayoutItem::margins() const
{
    return m_margins;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 172, as _ZN20QQStyleKitLayoutItem10setMarginsERK9QMarginsF
inline void QQStyleKitLayoutItem::setMargins(const QMarginsF &margins)
{
    if (m_margins == margins)
        return;

    m_margins = margins;
    emit marginsChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 181, as _ZNK20QQStyleKitLayoutItem9fillWidthEv
inline bool QQStyleKitLayoutItem::fillWidth() const
{
    return m_fillWidth;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 186, as _ZN20QQStyleKitLayoutItem12setFillWidthEb
inline void QQStyleKitLayoutItem::setFillWidth(bool fill)
{
    if (m_fillWidth == fill)
        return;

    m_fillWidth = fill;
    emit fillWidthChanged();
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 195, as _ZNK20QQStyleKitLayoutItem10fillHeightEv
inline bool QQStyleKitLayoutItem::fillHeight() const
{
    return m_fillHeight;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 200, as _ZN20QQStyleKitLayoutItem13setFillHeightEb
inline void QQStyleKitLayoutItem::setFillHeight(bool fill)
{
    if (m_fillHeight == fill)
        return;

    m_fillHeight = fill;
    emit fillHeightChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitLayoutItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQStyleKitLayoutItem10metaObjectEv(
    const QQStyleKitLayoutItem *self) {
  return self->metaObject();
}

//  void *QQStyleKitLayoutItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQStyleKitLayoutItem11qt_metacastEPKc(
    QQStyleKitLayoutItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQStyleKitLayoutItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQStyleKitLayoutItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQStyleKitLayoutItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQStyleKitLayoutItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQStyleKitLayoutItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitLayoutItem::tr(s, c, n));
}

//  QQStyleKitLayoutItem::QQStyleKitLayoutItem(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitLayoutItem *ritual_ZN20QQStyleKitLayoutItemC1EP7QObject(
    QObject *parent) {
  return new QQStyleKitLayoutItem(parent);
}

//  QQuickItem *QQStyleKitLayoutItem::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQStyleKitLayoutItem4itemEv(
    const QQStyleKitLayoutItem *self) {
  return self->item();
}

//  void QQStyleKitLayoutItem::setItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem7setItemEP10QQuickItem(
    QQStyleKitLayoutItem *self,
    QQuickItem *item) {
  self->setItem(item);
}

//  qreal QQStyleKitLayoutItem::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem1xEv(
    const QQStyleKitLayoutItem *self) {
  return self->x();
}

//  void QQStyleKitLayoutItem::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem4setXEd(
    QQStyleKitLayoutItem *self,
    qreal x) {
  self->setX(x);
}

//  qreal QQStyleKitLayoutItem::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem1yEv(
    const QQStyleKitLayoutItem *self) {
  return self->y();
}

//  void QQStyleKitLayoutItem::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem4setYEd(
    QQStyleKitLayoutItem *self,
    qreal y) {
  self->setY(y);
}

//  qreal QQStyleKitLayoutItem::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem5widthEv(
    const QQStyleKitLayoutItem *self) {
  return self->width();
}

//  void QQStyleKitLayoutItem::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem8setWidthEd(
    QQStyleKitLayoutItem *self,
    qreal width) {
  self->setWidth(width);
}

//  qreal QQStyleKitLayoutItem::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem6heightEv(
    const QQStyleKitLayoutItem *self) {
  return self->height();
}

//  void QQStyleKitLayoutItem::setHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem9setHeightEd(
    QQStyleKitLayoutItem *self,
    qreal height) {
  self->setHeight(height);
}

//  Qt::Alignment QQStyleKitLayoutItem::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQStyleKitLayoutItem9alignmentEv(
    const QQStyleKitLayoutItem *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QQStyleKitLayoutItem::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QQStyleKitLayoutItem *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QMarginsF QQStyleKitLayoutItem::margins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK20QQStyleKitLayoutItem7marginsEv(
    const QQStyleKitLayoutItem *self) {
  return new QMarginsF(self->margins());
}

//  void QQStyleKitLayoutItem::setMargins(const QMarginsF &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem10setMarginsERK9QMarginsF(
    QQStyleKitLayoutItem *self,
    const QMarginsF *margins) {
  self->setMargins(*margins);
}

//  bool QQStyleKitLayoutItem::fillWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQStyleKitLayoutItem9fillWidthEv(
    const QQStyleKitLayoutItem *self) {
  return self->fillWidth();
}

//  void QQStyleKitLayoutItem::setFillWidth(bool fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem12setFillWidthEb(
    QQStyleKitLayoutItem *self,
    bool fill) {
  self->setFillWidth(fill);
}

//  bool QQStyleKitLayoutItem::fillHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQStyleKitLayoutItem10fillHeightEv(
    const QQStyleKitLayoutItem *self) {
  return self->fillHeight();
}

//  void QQStyleKitLayoutItem::setFillHeight(bool fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem13setFillHeightEb(
    QQStyleKitLayoutItem *self,
    bool fill) {
  self->setFillHeight(fill);
}

//  void QQStyleKitLayoutItem::itemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem11itemChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::xChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem8xChangedEv(QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "xChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "xChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::yChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem8yChangedEv(QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "yChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "yChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::widthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem12widthChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "widthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "widthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::heightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem13heightChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "heightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "heightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::alignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem16alignmentChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "alignmentChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "alignmentChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::marginsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem14marginsChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "marginsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "marginsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::fillWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem16fillWidthChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fillWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fillWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQStyleKitLayoutItem::fillHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQStyleKitLayoutItem17fillHeightChangedEv(
    QQStyleKitLayoutItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQStyleKitLayoutItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fillHeightChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fillHeightChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
