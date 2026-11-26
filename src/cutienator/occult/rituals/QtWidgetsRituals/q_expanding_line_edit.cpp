//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QExpandingLineEdit' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <qplatformdefs.h>
#include <QtWidgets/qitemeditorfactory.h>
#include <QtWidgets/private/qitemeditorfactory_p.h>
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(datetimeedit)
#include <QtWidgets/qdatetimeedit.h>
#endif
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(spinbox)
#include <QtWidgets/qspinbox.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <limits.h>
#include <float.h>
#include <QtWidgets/qapplication.h>
#include <QtCore/qdebug.h>
#include <vector>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtWidgets__QExpandingLineEdit.cpp, line 1, as moc:QExpandingLineEdit
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QExpandingLineEditE_t {};
} // unnamed namespace

template <> constexpr inline auto QExpandingLineEdit::qt_create_metaobjectdata<qt_meta_tag_ZN18QExpandingLineEditE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QExpandingLineEdit",
        "resizeToContents",
        ""
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'resizeToContents'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QExpandingLineEdit, qt_meta_tag_ZN18QExpandingLineEditE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QExpandingLineEdit::staticMetaObject = { {
    QMetaObject::SuperData::link<QLineEdit::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QExpandingLineEditE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QExpandingLineEditE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QExpandingLineEditE_t>.metaTypes,
    nullptr
} };

void QExpandingLineEdit::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QExpandingLineEdit *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->resizeToContents(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QExpandingLineEdit::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QExpandingLineEdit::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QExpandingLineEditE_t>.strings))
        return static_cast<void*>(this);
    return QLineEdit::qt_metacast(_clname);
}

int QExpandingLineEdit::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QLineEdit::qt_metacall(_c, _id, _a);
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

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 517, as _ZN18QExpandingLineEdit11changeEventEP6QEvent
#if QT_CONFIG(lineedit)
inline void QExpandingLineEdit::changeEvent(QEvent *e)
{
    switch (e->type())
    {
    case QEvent::FontChange:
    case QEvent::StyleChange:
    case QEvent::ContentsRectChange:
        updateMinimumWidth();
        break;
    default:
        break;
    }

    QLineEdit::changeEvent(e);
}
#endif  // QT_CONFIG(lineedit)

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 546, as _ZN18QExpandingLineEdit16resizeToContentsEv
#if QT_CONFIG(lineedit)
inline void QExpandingLineEdit::resizeToContents()
{
    int oldWidth = width();
    if (originalWidth == -1)
        originalWidth = oldWidth;
    if (QWidget *parent = parentWidget()) {
        QPoint position = pos();
        int hintWidth = minimumWidth() + fontMetrics().horizontalAdvance(displayText());
        int parentWidth = parent->width();
        int maxWidth = isRightToLeft() ? position.x() + oldWidth : parentWidth - position.x();
        int newWidth = qBound(qMin(originalWidth, maxWidth), hintWidth, maxWidth);
        if (widgetOwnsGeometry)
            setMaximumWidth(newWidth);
        if (isRightToLeft())
            move(position.x() - newWidth + oldWidth, position.y());
        resize(newWidth, height());
    }
}
#endif  // QT_CONFIG(lineedit)

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 510, as _ZN18QExpandingLineEditC1EP7QWidget
#if QT_CONFIG(lineedit)
inline QExpandingLineEdit::QExpandingLineEdit(QWidget *parent)
    : QLineEdit(parent), originalWidth(-1), widgetOwnsGeometry(false)
{
    connect(this, SIGNAL(textChanged(QString)), this, SLOT(resizeToContents()));
    updateMinimumWidth();
}
#endif  // QT_CONFIG(lineedit)

//  from src/widgets/itemviews/qitemeditorfactory.cpp, line 533, as _ZN18QExpandingLineEdit18updateMinimumWidthEv
#if QT_CONFIG(lineedit)
inline void QExpandingLineEdit::updateMinimumWidth()
{
    const QMargins tm = textMargins();
    const QMargins cm = contentsMargins();
    const int width = tm.left() + tm.right() + cm.left() + cm.right() + 4 /*horizontalMargin in qlineedit.cpp*/;

    QStyleOptionFrame opt;
    initStyleOption(&opt);

    int minWidth = style()->sizeFromContents(QStyle::CT_LineEdit, &opt, QSize(width, 0), this).width();
    setMinimumWidth(minWidth);
}
#endif  // QT_CONFIG(lineedit)
//  -----------------------------------------------------------------------

//  Only a class built on QExpandingLineEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQExpandingLineEdit : QExpandingLineEdit {
  using QExpandingLineEdit::changeEvent;
};

//  const QMetaObject *QExpandingLineEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QExpandingLineEdit10metaObjectEv(
    const QExpandingLineEdit *self) {
  return self->metaObject();
}

//  void *QExpandingLineEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QExpandingLineEdit11qt_metacastEPKc(
    QExpandingLineEdit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QExpandingLineEdit::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QExpandingLineEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    QExpandingLineEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_CONFIG(lineedit)
//  QString QExpandingLineEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QExpandingLineEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QExpandingLineEdit::tr(s, c, n));
}
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
//  QExpandingLineEdit::QExpandingLineEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QExpandingLineEdit *ritual_ZN18QExpandingLineEditC1EP7QWidget(
    QWidget *parent) {
  return new QExpandingLineEdit(parent);
}
#endif  // QT_CONFIG(lineedit)

//  void QExpandingLineEdit::setWidgetOwnsGeometry(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit21setWidgetOwnsGeometryEb(
    QExpandingLineEdit *self,
    bool value) {
  self->setWidgetOwnsGeometry(value);
}

//  void QExpandingLineEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit11changeEventEP6QEvent(
    QExpandingLineEdit *self,
    QEvent *e) {
  self->changeEvent(e);
}

//  void QExpandingLineEdit::resizeToContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit16resizeToContentsEv(
    QExpandingLineEdit *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QExpandingLineEdit")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resizeToContents()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resizeToContents()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(lineedit)
//  void QExpandingLineEdit::updateMinimumWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QExpandingLineEdit18updateMinimumWidthEv(
    QExpandingLineEdit *self) {
  self->updateMinimumWidth();
}
#endif  // QT_CONFIG(lineedit)

#if QT_CONFIG(lineedit)
//  void QExpandingLineEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QExpandingLineEdit11changeEventEP6QEvent(
    QExpandingLineEdit *self,
    QEvent *e) {
  static_cast<OwnQExpandingLineEdit *>(self)->OwnQExpandingLineEdit::changeEvent(
      e);
}
#endif  // QT_CONFIG(lineedit)

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
