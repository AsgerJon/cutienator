//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextutil_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-26: moc's output for 'QQuickTextUtil' is pasted in, cut
//  from what the moc of Qt 6.12.0 writes for its header: Qt's library keeps
//  it to itself; added are 2 rituals that lean on what moc writes for a
//  class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
//  Also added by hand on 2026-11-25, instances of templates of the class: 3.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextutil_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquicktextutil_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuick/private/qquicktextinput_p.h>
#include <QtQuick/private/qquicktextinput_p_p.h>
#include <QtQuick/private/qquicktextedit_p.h>
#include <QtQuick/private/qquicktextedit_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickTextUtil.cpp, line 1, as moc:QQuickTextUtil
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN14QQuickTextUtilE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickTextUtil::qt_create_metaobjectdata<qt_meta_tag_ZN14QQuickTextUtilE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickTextUtil"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickTextUtil, qt_meta_tag_ZN14QQuickTextUtilE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickTextUtil::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QQuickTextUtilE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QQuickTextUtilE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN14QQuickTextUtilE_t>.metaTypes,
    nullptr
} };

void QQuickTextUtil::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickTextUtil *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickTextUtil::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickTextUtil::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN14QQuickTextUtilE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQuickTextUtil::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquicktextutil.cpp, line 48, as _ZN14QQuickTextUtil8alignedXEddi
inline qreal QQuickTextUtil::alignedX(const qreal textWidth, const qreal itemWidth, int alignment)
{
    qreal x = 0;
    switch (alignment) {
    case Qt::AlignLeft:
    case Qt::AlignJustify:
        break;
    case Qt::AlignRight:
        x = itemWidth - textWidth;
        break;
    case Qt::AlignHCenter:
        x = (itemWidth - textWidth) / 2;
        break;
    }
    return x;
}

//  from ../qtdeclarative/src/quick/items/qquicktextutil.cpp, line 65, as _ZN14QQuickTextUtil8alignedYEddi
inline qreal QQuickTextUtil::alignedY(const qreal textHeight, const qreal itemHeight, int alignment)
{
    qreal y = 0;
    switch (alignment) {
    case Qt::AlignTop:
        break;
    case Qt::AlignBottom:
        y = itemHeight - textHeight;
        break;
    case Qt::AlignVCenter:
        y = (itemHeight - textHeight) / 2;
        break;
    }
    return y;
}

//  from ../qtdeclarative/src/quick/items/qquicktextutil.cpp, line 15, as _ZN14QQuickTextUtil12createCursorEP13QQmlComponentP10QQuickItemRK6QRectFPKc
inline QQuickItem *QQuickTextUtil::createCursor(
        QQmlComponent *component, QQuickItem *parent, const QRectF &rectangle, const char *className)
{
    QQuickItem *item = nullptr;
    if (component->isReady()) {
        QQmlContext *creationContext = component->creationContext();

        if (QObject *object = component->beginCreate(creationContext
                ? creationContext
                : qmlContext(parent))) {
            if ((item = qobject_cast<QQuickItem *>(object))) {
                QQml_setParent_noEvent(item, parent);
                item->setParentItem(parent);
                item->setPosition(rectangle.topLeft());
                item->setHeight(rectangle.height());
            } else {
                qmlWarning(parent) << tr("%1 does not support loading non-visual cursor delegates.")
                        .arg(QString::fromUtf8(className));
            }
            component->completeCreate();
            if (parent->clip())
                QQuickItemPrivate::get(parent)->dirty(QQuickItemPrivate::Size);
            return item;
        }
    } else if (component->isLoading()) {
        QObject::connect(component, SIGNAL(statusChanged(QQmlComponent::Status)),
                parent, SLOT(createCursor()), Qt::UniqueConnection);
        return item;
    }
    qmlWarning(parent, component->errors()) << tr("Could not load cursor delegate");
    return item;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickTextUtil::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTextUtil10metaObjectEv(
    const QQuickTextUtil *self) {
  return self->metaObject();
}

//  void *QQuickTextUtil::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickTextUtil11qt_metacastEPKc(
    QQuickTextUtil *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextUtil::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextUtil11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextUtil *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTextUtil::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTextUtil2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextUtil::tr(s, c, n));
}

//  qreal QQuickTextUtil::alignedX(qreal textWidth, qreal itemWidth, int
//      alignment)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QQuickTextUtil8alignedXEddi(
    qreal textWidth,
    qreal itemWidth,
    int alignment) {
  return QQuickTextUtil::alignedX(textWidth, itemWidth, alignment);
}

//  qreal QQuickTextUtil::alignedY(qreal textHeight, qreal itemHeight, int
//      alignment)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QQuickTextUtil8alignedYEddi(
    qreal textHeight,
    qreal itemHeight,
    int alignment) {
  return QQuickTextUtil::alignedY(textHeight, itemHeight, alignment);
}

//  QQuickItem *QQuickTextUtil::createCursor(QQmlComponent *component,
//      QQuickItem *parent, const QRectF &cursorRectangle, const char
//      *className)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN14QQuickTextUtil12createCursorEP13QQmlComponentP10QQuickItemRK6QRectFPKc(
    QQmlComponent *component,
    QQuickItem *parent,
    const QRectF *cursorRectangle,
    const char *className) {
  return QQuickTextUtil::createCursor(
      component,
      parent,
      *cursorRectangle,
      className);
}

//  static QQuickText::RenderType
//      QQuickTextUtil::textRenderType<QQuickText>()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextUtil14textRenderTypeI10QQuickTextEENT_10RenderTypeEv() {
  return static_cast<int>(
      QQuickTextUtil::textRenderType<QQuickText>());
}

//  static QQuickTextEdit::RenderType
//      QQuickTextUtil::textRenderType<QQuickTextEdit>()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextUtil14textRenderTypeI14QQuickTextEditEENT_10RenderTypeEv() {
  return static_cast<int>(
      QQuickTextUtil::textRenderType<QQuickTextEdit>());
}

//  static QQuickTextInput::RenderType
//      QQuickTextUtil::textRenderType<QQuickTextInput>()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextUtil14textRenderTypeI15QQuickTextInputEENT_10RenderTypeEv() {
  return static_cast<int>(
      QQuickTextUtil::textRenderType<QQuickTextInput>());
}
