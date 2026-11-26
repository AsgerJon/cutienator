//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfu
//  siondial_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickFusionDial' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2FusionStyleImpl/QtQuickControls2FusionStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfusiondial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickControls2FusionStyleImpl/private/qquickfusiondial_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/private/qmath_p.h>
#include <QtQuick/private/qquickpalette_p.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuickControls2FusionStyleImpl__QQuickFusionDial.cpp, line 1, as moc:QQuickFusionDial
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN16QQuickFusionDialE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickFusionDial::qt_create_metaobjectdata<qt_meta_tag_ZN16QQuickFusionDialE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickFusionDial",
        "QML.Element",
        "DialImpl",
        "QML.AddedInVersion",
        "515",
        "highlight"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
        // property 'highlight'
        QtMocHelpers::PropertyData<bool>(5, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet | QMC::Final),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickFusionDial, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickFusionDial::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickPaintedItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QQuickFusionDialE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QQuickFusionDialE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN16QQuickFusionDialE_t>.metaTypes,
    nullptr
} };

void QQuickFusionDial::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickFusionDial *>(_o);
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<bool*>(_v) = _t->highlight(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setHighlight(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickFusionDial::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickFusionDial::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN16QQuickFusionDialE_t>.strings))
        return static_cast<void*>(this);
    return QQuickPaintedItem::qt_metacast(_clname);
}

int QQuickFusionDial::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickPaintedItem::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 34, as _ZN16QQuickFusionDial5paintEP8QPainter
inline void QQuickFusionDial::paint(QPainter *painter)
{
    const int width = QQuickItem::width();
    const int height = QQuickItem::height();
    if (width <= 0 || height <= 0 || !isVisible())
        return;

    const bool enabled = isEnabled();
    qreal r = qMin(width, height) / 2.0;
    r -= r/50;
    const qreal penSize = r/20.0;

    painter->setRenderHint(QPainter::Antialiasing);

    const qreal d_ = r / 6;
    const qreal dx = d_ + (width - 2 * r) / 2 + 1;
    const qreal dy = d_ + (height - 2 * r) / 2 + 1;

    QRectF br = QRectF(dx + 0.5, dy + 0.5,
                       int(r * 2 - 2 * d_ - 2),
                       int(r * 2 - 2 * d_ - 2));
    QColor buttonColor = QQuickItemPrivate::get(this)->palette()->button().toHsv();
    buttonColor.setHsv(buttonColor .hue(),
                       qMin(140, buttonColor .saturation()),
                       qMax(180, buttonColor.value()));

    if (enabled) {
        // Drop shadow
        qreal shadowSize = qMax(1.0, penSize/2.0);
        QRectF shadowRect= br.adjusted(-2*shadowSize, -2*shadowSize,
                                       2*shadowSize, 2*shadowSize);
        QRadialGradient shadowGradient(shadowRect.center().x(),
                                       shadowRect.center().y(), shadowRect.width()/2.0,
                                       shadowRect.center().x(), shadowRect.center().y());
        shadowGradient.setColorAt(qreal(0.91), QColor(0, 0, 0, 40));
        shadowGradient.setColorAt(qreal(1.0), Qt::transparent);
        painter->setBrush(shadowGradient);
        painter->setPen(Qt::NoPen);
        painter->translate(shadowSize, shadowSize);
        painter->drawEllipse(shadowRect);
        painter->translate(-shadowSize, -shadowSize);

        // Main gradient
        QRadialGradient gradient(br.center().x() - br.width()/3, dy,
                                 br.width()*1.3, br.center().x(),
                                 br.center().y() - br.height()/2);
        gradient.setColorAt(0, buttonColor.lighter(110));
        gradient.setColorAt(qreal(0.5), buttonColor);
        gradient.setColorAt(qreal(0.501), buttonColor.darker(102));
        gradient.setColorAt(1, buttonColor.darker(115));
        painter->setBrush(gradient);
    } else {
        painter->setBrush(Qt::NoBrush);
    }

    painter->setPen(QPen(buttonColor.darker(280)));
    painter->drawEllipse(br);
    painter->setBrush(Qt::NoBrush);
    painter->setPen(buttonColor.lighter(110));
    painter->drawEllipse(br.adjusted(1, 1, -1, -1));

    if (m_highlight) {
        QColor highlight = QQuickItemPrivate::get(this)->palette()->highlight().toHsv();
        highlight.setHsv(highlight.hue(),
                         qMin(160, highlight.saturation()),
                         qMax(230, highlight.value()));
        highlight.setAlpha(127);
        painter->setPen(QPen(highlight, 2.0));
        painter->setBrush(Qt::NoBrush);
        painter->drawEllipse(br.adjusted(-1, -1, 1, 1));
    }
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 14, as _ZN16QQuickFusionDialC1EP10QQuickItem
inline QQuickFusionDial::QQuickFusionDial(QQuickItem *parent)
    : QQuickPaintedItem(parent)
{
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 19, as _ZNK16QQuickFusionDial9highlightEv
inline bool QQuickFusionDial::highlight() const
{
    return m_highlight;
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 24, as _ZN16QQuickFusionDial12setHighlightEb
inline void QQuickFusionDial::setHighlight(bool highlight)
{
    if (m_highlight == highlight)
        return;

    m_highlight = highlight;
    update();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickFusionDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickFusionDial10metaObjectEv(
    const QQuickFusionDial *self) {
  return self->metaObject();
}

//  void *QQuickFusionDial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickFusionDial11qt_metacastEPKc(
    QQuickFusionDial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFusionDial::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickFusionDial11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFusionDial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFusionDial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickFusionDial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFusionDial::tr(s, c, n));
}

//  QQuickFusionDial::QQuickFusionDial(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFusionDial *ritual_ZN16QQuickFusionDialC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFusionDial(parent);
}

//  bool QQuickFusionDial::highlight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickFusionDial9highlightEv(const QQuickFusionDial *self) {
  return self->highlight();
}

//  void QQuickFusionDial::setHighlight(bool highlight)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFusionDial12setHighlightEb(
    QQuickFusionDial *self,
    bool highlight) {
  self->setHighlight(highlight);
}

//  void QQuickFusionDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFusionDial5paintEP8QPainter(
    QQuickFusionDial *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickFusionDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFusionDial5paintEP8QPainter(
    QQuickFusionDial *self,
    QPainter *painter) {
  self->QQuickFusionDial::paint(painter);
}
