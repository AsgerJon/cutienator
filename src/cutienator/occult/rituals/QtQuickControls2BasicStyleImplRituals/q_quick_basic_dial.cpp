//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasi
//  cdial_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickBasicDial' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2BasicStyleImpl/QtQuickControls2BasicStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasicdial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickControls2BasicStyleImpl/private/qquickbasicdial_p.h>
#include <QtCore/qmath.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuickControls2BasicStyleImpl__QQuickBasicDial.cpp, line 1, as moc:QQuickBasicDial
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QQuickBasicDialE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickBasicDial::qt_create_metaobjectdata<qt_meta_tag_ZN15QQuickBasicDialE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickBasicDial",
        "QML.Element",
        "DialImpl",
        "QML.AddedInVersion",
        "512",
        "progress",
        "startAngle",
        "endAngle",
        "color",
        "QColor"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
        // property 'progress'
        QtMocHelpers::PropertyData<qreal>(5, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final),
        // property 'startAngle'
        QtMocHelpers::PropertyData<qreal>(6, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final),
        // property 'endAngle'
        QtMocHelpers::PropertyData<qreal>(7, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final),
        // property 'color'
        QtMocHelpers::PropertyData<QColor>(8, 0x80000000 | 9, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickBasicDial, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickBasicDial::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickPaintedItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QQuickBasicDialE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QQuickBasicDialE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QQuickBasicDialE_t>.metaTypes,
    nullptr
} };

void QQuickBasicDial::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickBasicDial *>(_o);
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<qreal*>(_v) = _t->progress(); break;
        case 1: *reinterpret_cast<qreal*>(_v) = _t->startAngle(); break;
        case 2: *reinterpret_cast<qreal*>(_v) = _t->endAngle(); break;
        case 3: *reinterpret_cast<QColor*>(_v) = _t->color(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setProgress(*reinterpret_cast<qreal*>(_v)); break;
        case 1: _t->setStartAngle(*reinterpret_cast<qreal*>(_v)); break;
        case 2: _t->setEndAngle(*reinterpret_cast<qreal*>(_v)); break;
        case 3: _t->setColor(*reinterpret_cast<QColor*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickBasicDial::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickBasicDial::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QQuickBasicDialE_t>.strings))
        return static_cast<void*>(this);
    return QQuickPaintedItem::qt_metacast(_clname);
}

int QQuickBasicDial::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickPaintedItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 75, as _ZN15QQuickBasicDial5paintEP8QPainter
inline void QQuickBasicDial::paint(QPainter *painter)
{
    if (width() <= 0 || height() <= 0)
        return;

    QPen pen(m_color);
    pen.setWidth(8);
    pen.setCapStyle(Qt::FlatCap);
    painter->setPen(pen);

    const QRectF bounds = boundingRect();
    const qreal smallest = qMin(bounds.width(), bounds.height());
    QRectF rect = QRectF(pen.widthF() / 2.0 + 1, pen.widthF() / 2.0 + 1, smallest - pen.widthF() - 2, smallest - pen.widthF() - 2);
    rect.moveCenter(bounds.center());

    // Make sure the arc is aligned to whole pixels.
    if (rect.x() - int(rect.x()) > 0)
        rect.setX(qCeil(rect.x()));
    if (rect.y() - int(rect.y()) > 0)
        rect.setY(qCeil(rect.y()));
    if (rect.width() - int(rect.width()) > 0)
        rect.setWidth(qFloor(rect.width()));
    if (rect.height() - int(rect.height()) > 0)
        rect.setHeight(qFloor(rect.height()));

    painter->setRenderHint(QPainter::Antialiasing);

    const qreal startAngle = 90. - m_startAngle;
    const qreal spanAngle = m_progress * (m_startAngle - m_endAngle);
    QPainterPath path;
    path.arcMoveTo(rect, startAngle);
    path.arcTo(rect, startAngle, spanAngle);
    painter->drawPath(path);

    rect.adjust(-pen.widthF() / 2.0, -pen.widthF() / 2.0, pen.widthF() / 2.0, pen.widthF() / 2.0);
    pen.setWidth(1);
    painter->setPen(pen);

    path = QPainterPath();
    path.arcMoveTo(rect, 0);
    path.arcTo(rect, 0, 360);
    painter->drawPath(path);
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 14, as _ZN15QQuickBasicDialC1EP10QQuickItem
inline QQuickBasicDial::QQuickBasicDial(QQuickItem *parent) :
    QQuickPaintedItem(parent)
{
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 19, as _ZNK15QQuickBasicDial8progressEv
inline qreal QQuickBasicDial::progress() const
{
    return m_progress;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 24, as _ZN15QQuickBasicDial11setProgressEd
inline void QQuickBasicDial::setProgress(qreal progress)
{
    if (progress == m_progress)
        return;

    m_progress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 33, as _ZNK15QQuickBasicDial10startAngleEv
inline qreal QQuickBasicDial::startAngle() const
{
    return m_startAngle;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 38, as _ZN15QQuickBasicDial13setStartAngleEd
inline void QQuickBasicDial::setStartAngle(qreal startAngle)
{
    if (startAngle == m_startAngle)
        return;

    m_startAngle = startAngle;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 47, as _ZNK15QQuickBasicDial8endAngleEv
inline qreal QQuickBasicDial::endAngle() const
{
    return m_endAngle;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 52, as _ZN15QQuickBasicDial11setEndAngleEd
inline void QQuickBasicDial::setEndAngle(qreal endAngle)
{
    if (endAngle == m_endAngle)
        return;

    m_endAngle = endAngle;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 61, as _ZNK15QQuickBasicDial5colorEv
inline QColor QQuickBasicDial::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 66, as _ZN15QQuickBasicDial8setColorERK6QColor
inline void QQuickBasicDial::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickBasicDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickBasicDial10metaObjectEv(
    const QQuickBasicDial *self) {
  return self->metaObject();
}

//  void *QQuickBasicDial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickBasicDial11qt_metacastEPKc(
    QQuickBasicDial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBasicDial::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickBasicDial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBasicDial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBasicDial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickBasicDial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBasicDial::tr(s, c, n));
}

//  QQuickBasicDial::QQuickBasicDial(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickBasicDial *ritual_ZN15QQuickBasicDialC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickBasicDial(parent);
}

//  qreal QQuickBasicDial::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickBasicDial8progressEv(const QQuickBasicDial *self) {
  return self->progress();
}

//  void QQuickBasicDial::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial11setProgressEd(
    QQuickBasicDial *self,
    qreal progress) {
  self->setProgress(progress);
}

//  qreal QQuickBasicDial::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickBasicDial10startAngleEv(
    const QQuickBasicDial *self) {
  return self->startAngle();
}

//  void QQuickBasicDial::setStartAngle(qreal startAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial13setStartAngleEd(
    QQuickBasicDial *self,
    qreal startAngle) {
  self->setStartAngle(startAngle);
}

//  qreal QQuickBasicDial::endAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickBasicDial8endAngleEv(const QQuickBasicDial *self) {
  return self->endAngle();
}

//  void QQuickBasicDial::setEndAngle(qreal endAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial11setEndAngleEd(
    QQuickBasicDial *self,
    qreal endAngle) {
  self->setEndAngle(endAngle);
}

//  QColor QQuickBasicDial::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickBasicDial5colorEv(const QQuickBasicDial *self) {
  return new QColor(self->color());
}

//  void QQuickBasicDial::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial8setColorERK6QColor(
    QQuickBasicDial *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickBasicDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial5paintEP8QPainter(
    QQuickBasicDial *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickBasicDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickBasicDial5paintEP8QPainter(
    QQuickBasicDial *self,
    QPainter *painter) {
  self->QQuickBasicDial::paint(painter);
}
