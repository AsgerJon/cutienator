//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QLineEditIconButton' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 4 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(toolbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemview.h>
#endif
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#if QT_CONFIG(action)
#  include <QtWidgets/qwidgetaction.h>
#endif
#include <QtGui/qclipboard.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#ifndef QT_NO_IM
#include <QtGui/qinputmethod.h>
#include <QtCore/qlist.h>
#endif
#include <QtGui/qpainter.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/qvalidator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWidgets__QLineEditIconButton.cpp, line 1, as moc:QLineEditIconButton
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN19QLineEditIconButtonE_t {};
} // unnamed namespace

template <> constexpr inline auto QLineEditIconButton::qt_create_metaobjectdata<qt_meta_tag_ZN19QLineEditIconButtonE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QLineEditIconButton",
        "updateCursor",
        "",
        "onAnimationFinished",
        "opacity"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'updateCursor'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'onAnimationFinished'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'opacity'
        QtMocHelpers::PropertyData<qreal>(4, QMetaType::QReal, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QLineEditIconButton, qt_meta_tag_ZN19QLineEditIconButtonE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QLineEditIconButton::staticMetaObject = { {
    QMetaObject::SuperData::link<QToolButton::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QLineEditIconButtonE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QLineEditIconButtonE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN19QLineEditIconButtonE_t>.metaTypes,
    nullptr
} };

void QLineEditIconButton::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QLineEditIconButton *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->updateCursor(); break;
        case 1: _t->onAnimationFinished(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<qreal*>(_v) = _t->opacity(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: _t->setOpacity(*reinterpret_cast<qreal*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QLineEditIconButton::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QLineEditIconButton::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QLineEditIconButtonE_t>.strings))
        return static_cast<void*>(this);
    return QToolButton::qt_metacast(_clname);
}

int QLineEditIconButton::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QToolButton::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 1;
    }
    return _id;
}
QT_WARNING_POP

//  from src/widgets/widgets/qlineedit_p.cpp, line 347, as _ZN19QLineEditIconButton10paintEventEP11QPaintEvent
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::paintEvent(QPaintEvent *)
{
    QPainter painter(this);
    QIcon::Mode mode = QIcon::Disabled;
    if (isEnabled())
        mode = isDown() ? QIcon::Active : QIcon::Normal;
    const QLineEditPrivate *lep = lineEditPrivate();
    const int iconWidth = lep ? lep->sideWidgetParameters().iconSize : 16;
    const QSize iconSize(iconWidth, iconWidth);
    QRect pixmapRect = QRect(QPoint(0, 0), iconSize);
    pixmapRect.moveCenter(rect().center());
    painter.setOpacity(m_opacity);
    icon().paint(&painter, pixmapRect, Qt::AlignCenter, mode, QIcon::Off);
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 362, as _ZN19QLineEditIconButton11actionEventEP12QActionEvent
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::actionEvent(QActionEvent *e)
{
    switch (e->type()) {
    case QEvent::ActionChanged: {
        const auto *action = e->action();
        if (isVisibleTo(parentWidget()) != action->isVisible()) {
            setVisible(action->isVisible());
            if (QLineEditPrivate *lep = lineEditPrivate())
                lep->positionSideWidgets();
        }
    }
        break;
    default:
        break;
    }
    QToolButton::actionEvent(e);
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 438, as _ZN19QLineEditIconButton12updateCursorEv
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::updateCursor()
{
#ifndef QT_NO_CURSOR
    setCursor(qFuzzyCompare(m_opacity, qreal(1.0)) || !parentWidget() ? QCursor(Qt::ArrowCursor) : parentWidget()->cursor());
#endif
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 400, as _ZN19QLineEditIconButton19onAnimationFinishedEv
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::onAnimationFinished()
{
    if (shouldHideWithText() && isVisible() && m_fadingOut) {
        hide();
        m_fadingOut = false;

        // Invalidate previous geometry to take into account new size of side widgets
        if (auto le = lineEditPrivate())
            le->updateGeometry_helper(true);
    }
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 521, as _ZN16QLineEditPrivate19positionSideWidgetsEv
inline void QLineEditPrivate::positionSideWidgets()
{
    Q_Q(QLineEdit);
    if (hasSideWidgets()) {
        const QRect contentRect = q->rect();
        const SideWidgetParameters p = sideWidgetParameters();
        const int delta = p.margin + p.widgetWidth;
        QRect widgetGeometry(QPoint(p.margin, (contentRect.height() - p.widgetHeight) / 2),
                             QSize(p.widgetWidth, p.widgetHeight));
        for (const SideWidgetEntry &e : leftSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() + delta);
#else
            Q_UNUSED(delta);
#endif
        }
        widgetGeometry.moveLeft(contentRect.width() - p.widgetWidth - p.margin);
        for (const SideWidgetEntry &e : rightSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() - delta);
#endif
        }
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 488, as _ZNK16QLineEditPrivate20sideWidgetParametersEv
inline QLineEditPrivate::SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
{
    Q_Q(const QLineEdit);
    SideWidgetParameters result;
    result.iconSize = q->style()->pixelMetric(QStyle::PM_LineEditIconSize, nullptr, q);
    result.margin = q->style()->pixelMetric(QStyle::PM_LineEditIconMargin, nullptr, q);
    result.widgetWidth = result.iconSize + 6;
    result.widgetHeight = result.iconSize + 2;
    return result;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 334, as _ZN19QLineEditIconButtonC1EP7QWidget
#if QT_CONFIG(toolbutton)
inline QLineEditIconButton::QLineEditIconButton(QWidget *parent)
    : QToolButton(parent)
    , m_opacity(0)
{
    setFocusPolicy(Qt::NoFocus);
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 380, as _ZN19QLineEditIconButton10setOpacityEd
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::setOpacity(qreal value)
{
    if (!qFuzzyCompare(m_opacity, value)) {
        m_opacity = value;
        updateCursor();
        update();
    }
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 412, as _ZN19QLineEditIconButton11animateShowEb
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::animateShow(bool visible)
{
    m_fadingOut = !visible;

    if (shouldHideWithText() && !isVisible()) {
        show();

        // Invalidate previous geometry to take into account new size of side widgets
        if (auto le = lineEditPrivate())
            le->updateGeometry_helper(true);
    }

    startOpacityAnimation(visible ? 1.0 : 0.0);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 390, as _ZNK19QLineEditIconButton18shouldHideWithTextEv
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline bool QLineEditIconButton::shouldHideWithText() const
{
    return m_hideWithText;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 395, as _ZN19QLineEditIconButton15setHideWithTextEb
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::setHideWithText(bool hide)
{
    m_hideWithText = hide;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 427, as _ZN19QLineEditIconButton21startOpacityAnimationEd
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::startOpacityAnimation(qreal endValue)
{
    QPropertyAnimation *animation = new QPropertyAnimation(this, QByteArrayLiteral("opacity"), this);
    connect(animation, &QPropertyAnimation::finished, this, &QLineEditIconButton::onAnimationFinished);

    animation->setDuration(160);
    animation->setEndValue(endValue);
    animation->start(QAbstractAnimation::DeleteWhenStopped);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 341, as _ZNK19QLineEditIconButton15lineEditPrivateEv
#if QT_CONFIG(toolbutton)
inline QLineEditPrivate *QLineEditIconButton::lineEditPrivate() const
{
    QLineEdit *le = qobject_cast<QLineEdit *>(parentWidget());
    return le ? static_cast<QLineEditPrivate *>(qt_widget_private(le)) : nullptr;
}
#endif  // QT_CONFIG(toolbutton)
//  -----------------------------------------------------------------------

//  Only a class built on QLineEditIconButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLineEditIconButton : QLineEditIconButton {
  using QLineEditIconButton::actionEvent;
  using QLineEditIconButton::paintEvent;
};

//  const QMetaObject *QLineEditIconButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QLineEditIconButton10metaObjectEv(
    const QLineEditIconButton *self) {
  return self->metaObject();
}

//  void *QLineEditIconButton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QLineEditIconButton11qt_metacastEPKc(
    QLineEditIconButton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLineEditIconButton::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QLineEditIconButton11qt_metacallEN11QMetaObject4CallEiPPv(
    QLineEditIconButton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
//  QString QLineEditIconButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QLineEditIconButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLineEditIconButton::tr(s, c, n));
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
//  QLineEditIconButton::QLineEditIconButton(QWidget *parent)
extern "C" Q_DECL_EXPORT
QLineEditIconButton *ritual_ZN19QLineEditIconButtonC1EP7QWidget(
    QWidget *parent) {
  return new QLineEditIconButton(parent);
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  qreal QLineEditIconButton::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QLineEditIconButton7opacityEv(
    const QLineEditIconButton *self) {
  return self->opacity();
}

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::setOpacity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton10setOpacityEd(
    QLineEditIconButton *self,
    qreal value) {
  self->setOpacity(value);
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::animateShow(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton11animateShowEb(
    QLineEditIconButton *self,
    bool visible) {
  self->animateShow(visible);
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  bool QLineEditIconButton::shouldHideWithText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QLineEditIconButton18shouldHideWithTextEv(
    const QLineEditIconButton *self) {
  return self->shouldHideWithText();
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::setHideWithText(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton15setHideWithTextEb(
    QLineEditIconButton *self,
    bool hide) {
  self->setHideWithText(hide);
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  bool QLineEditIconButton::needsSpace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QLineEditIconButton10needsSpaceEv(
    const QLineEditIconButton *self) {
  return self->needsSpace();
}
#endif  // QT_CONFIG(animation)

//  void QLineEditIconButton::actionEvent(QActionEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton11actionEventEP12QActionEvent(
    QLineEditIconButton *self,
    QActionEvent *e) {
  self->actionEvent(e);
}

//  void QLineEditIconButton::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton10paintEventEP11QPaintEvent(
    QLineEditIconButton *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QLineEditIconButton::updateCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton12updateCursorEv(
    QLineEditIconButton *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLineEditIconButton")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateCursor()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateCursor()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(animation)
//  void QLineEditIconButton::onAnimationFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton19onAnimationFinishedEv(
    QLineEditIconButton *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLineEditIconButton")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onAnimationFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onAnimationFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::startOpacityAnimation(qreal endValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLineEditIconButton21startOpacityAnimationEd(
    QLineEditIconButton *self,
    qreal endValue) {
  self->startOpacityAnimation(endValue);
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(toolbutton)
//  QLineEditPrivate *QLineEditIconButton::lineEditPrivate() const
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZNK19QLineEditIconButton15lineEditPrivateEv(
    const QLineEditIconButton *self) {
  return self->lineEditPrivate();
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::actionEvent(QActionEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLineEditIconButton11actionEventEP12QActionEvent(
    QLineEditIconButton *self,
    QActionEvent *e) {
  static_cast<OwnQLineEditIconButton *>(self)->OwnQLineEditIconButton::actionEvent(
      e);
}
#endif  // QT_CONFIG(toolbutton)

#if QT_CONFIG(toolbutton)
//  void QLineEditIconButton::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QLineEditIconButton10paintEventEP11QPaintEvent(
    QLineEditIconButton *self,
    QPaintEvent *event) {
  static_cast<OwnQLineEditIconButton *>(self)->OwnQLineEditIconButton::paintEvent(
      event);
}
#endif  // QT_CONFIG(toolbutton)

#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(lineedit)
