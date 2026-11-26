//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbarextension_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QToolBarExtension' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(toolbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbarextension_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/private/qtoolbarextension_p.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qstyleoption.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtWidgets__QToolBarExtension.cpp, line 1, as moc:QToolBarExtension
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN17QToolBarExtensionE_t {};
} // unnamed namespace

template <> constexpr inline auto QToolBarExtension::qt_create_metaobjectdata<qt_meta_tag_ZN17QToolBarExtensionE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QToolBarExtension",
        "setOrientation",
        "",
        "Qt::Orientation",
        "o"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'setOrientation'
        QtMocHelpers::SlotData<void(Qt::Orientation)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QToolBarExtension, qt_meta_tag_ZN17QToolBarExtensionE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QToolBarExtension::staticMetaObject = { {
    QMetaObject::SuperData::link<QToolButton::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QToolBarExtensionE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QToolBarExtensionE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN17QToolBarExtensionE_t>.metaTypes,
    nullptr
} };

void QToolBarExtension::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QToolBarExtension *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->setOrientation((*reinterpret_cast<std::add_pointer_t<Qt::Orientation>>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject *QToolBarExtension::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QToolBarExtension::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN17QToolBarExtensionE_t>.strings))
        return static_cast<void*>(this);
    return QToolButton::qt_metacast(_clname);
}

int QToolBarExtension::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QToolButton::qt_metacall(_c, _id, _a);
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

//  from src/widgets/widgets/qtoolbarextension.cpp, line 38, as _ZN17QToolBarExtension10paintEventEP11QPaintEvent
inline void QToolBarExtension::paintEvent(QPaintEvent *)
{
    QStylePainter p(this);
    QStyleOptionToolButton opt;
    initStyleOption(&opt);
    // We do not need to draw both extension arrows
    opt.features &= ~QStyleOptionToolButton::HasMenu;
    p.drawComplexControl(QStyle::CC_ToolButton, opt);
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 26, as _ZN17QToolBarExtension14setOrientationEN2Qt11OrientationE
inline void QToolBarExtension::setOrientation(Qt::Orientation o)
{
    QStyleOption opt;
    opt.initFrom(this);
    if (o == Qt::Horizontal) {
        setIcon(style()->standardIcon(QStyle::SP_ToolBarHorizontalExtensionButton, &opt, this));
    } else {
        setIcon(style()->standardIcon(QStyle::SP_ToolBarVerticalExtensionButton, &opt, this));
    }
    m_orientation = o;
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 57, as _ZN17QToolBarExtension5eventEP6QEvent
inline bool QToolBarExtension::event(QEvent *event)
{
    switch (event->type()) {
    case QEvent::LayoutDirectionChange:
        setOrientation(m_orientation);
        break;
    default:
        break;
    }
    return QToolButton::event(event);
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 49, as _ZNK17QToolBarExtension8sizeHintEv
inline QSize QToolBarExtension::sizeHint() const
{
    QStyleOption opt;
    opt.initFrom(this);
    const int ext = style()->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, this);
    return QSize(ext, ext);
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 15, as _ZN17QToolBarExtensionC1EP7QWidget
inline QToolBarExtension::QToolBarExtension(QWidget *parent)
    : QToolButton(parent)
    , m_orientation(Qt::Horizontal)
{
    setObjectName("qt_toolbar_ext_button"_L1);
    setAutoRaise(true);
    setOrientation(m_orientation);
    setSizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
    setCheckable(true);
}
//  -----------------------------------------------------------------------

//  Only a class built on QToolBarExtension may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQToolBarExtension : QToolBarExtension {
  using QToolBarExtension::event;
};

//  const QMetaObject *QToolBarExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QToolBarExtension10metaObjectEv(
    const QToolBarExtension *self) {
  return self->metaObject();
}

//  void *QToolBarExtension::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QToolBarExtension11qt_metacastEPKc(
    QToolBarExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QToolBarExtension::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QToolBarExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    QToolBarExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QToolBarExtension::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QToolBarExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QToolBarExtension::tr(s, c, n));
}

//  QToolBarExtension::QToolBarExtension(QWidget *parent)
extern "C" Q_DECL_EXPORT
QToolBarExtension *ritual_ZN17QToolBarExtensionC1EP7QWidget(
    QWidget *parent) {
  return new QToolBarExtension(parent);
}

//  void QToolBarExtension::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QToolBarExtension10paintEventEP11QPaintEvent(
    QToolBarExtension *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  QSize QToolBarExtension::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QToolBarExtension8sizeHintEv(
    const QToolBarExtension *self) {
  return new QSize(self->sizeHint());
}

//  void QToolBarExtension::setOrientation(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QToolBarExtension14setOrientationEN2Qt11OrientationE(
    QToolBarExtension *self,
    Qt::Orientation o) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QToolBarExtension")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setOrientation(Qt::Orientation)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setOrientation(Qt::Orientation)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&o)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QToolBarExtension::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QToolBarExtension5eventEP6QEvent(
    QToolBarExtension *self,
    QEvent *e) {
  return self->event(e);
}

//  void QToolBarExtension::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QToolBarExtension10paintEventEP11QPaintEvent(
    QToolBarExtension *self,
    QPaintEvent *a0) {
  self->QToolBarExtension::paintEvent(a0);
}

//  QSize QToolBarExtension::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QToolBarExtension8sizeHintEv(
    const QToolBarExtension *self) {
  return new QSize(self->QToolBarExtension::sizeHint());
}

//  bool QToolBarExtension::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QToolBarExtension5eventEP6QEvent(
    QToolBarExtension *self,
    QEvent *e) {
  return static_cast<OwnQToolBarExtension *>(self)->OwnQToolBarExtension::event(
      e);
}

#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(toolbutton)
