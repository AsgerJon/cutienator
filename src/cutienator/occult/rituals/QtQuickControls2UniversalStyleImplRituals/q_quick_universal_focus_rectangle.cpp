//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qq
//  uickuniversalfocusrectangle_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickUniversalFocusRectangle' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2UniversalStyleImpl/QtQuickControls2UniversalStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qquickuniversalfocusrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickControls2UniversalStyleImpl/private/qquickuniversalfocusrectangle_p.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpixmapcache.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuickControls2UniversalStyleImpl__QQuickUniversalFocusRectangle.cpp, line 1, as moc:QQuickUniversalFocusRectangle
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN29QQuickUniversalFocusRectangleE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickUniversalFocusRectangle::qt_create_metaobjectdata<qt_meta_tag_ZN29QQuickUniversalFocusRectangleE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickUniversalFocusRectangle",
        "QML.Element",
        "FocusRectangle",
        "QML.AddedInVersion",
        "512"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickUniversalFocusRectangle, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickUniversalFocusRectangle::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickPaintedItem::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickUniversalFocusRectangleE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickUniversalFocusRectangleE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN29QQuickUniversalFocusRectangleE_t>.metaTypes,
    nullptr
} };

void QQuickUniversalFocusRectangle::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickUniversalFocusRectangle *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickUniversalFocusRectangle::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickUniversalFocusRectangle::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN29QQuickUniversalFocusRectangleE_t>.strings))
        return static_cast<void*>(this);
    return QQuickPaintedItem::qt_metacast(_clname);
}

int QQuickUniversalFocusRectangle::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickPaintedItem::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalfocusrectangle.cpp, line 20, as _ZN29QQuickUniversalFocusRectangle5paintEP8QPainter
inline void QQuickUniversalFocusRectangle::paint(QPainter *painter)
{
    if (!isVisible() || width() <= 0 || height() <= 0)
        return;

    QRect bounds = boundingRect().toAlignedRect();
    const int boundsWidth = bounds.width();
    const int boundsHeight = bounds.width();
    const QString key = QStringLiteral("qquickuniversalfocusrectangle_%1_%2").arg(QString::number(boundsWidth), QString::number(boundsHeight));

    QPixmap pixmap(boundsWidth, boundsHeight);
    if (!QPixmapCache::find(key, &pixmap)) {
        bounds.adjust(0, 0, -1, -1);
        pixmap.fill(Qt::transparent);
        QPainter p(&pixmap);

        QPen pen;
        pen.setWidth(1);
        pen.setColor(Qt::white);
        p.setPen(pen);
        p.drawRect(bounds);

        pen.setColor(Qt::black);
        pen.setDashPattern(QList<qreal>(2, 1));
        p.setPen(pen);
        p.drawRect(bounds);

        QPixmapCache::insert(key, pixmap);
    }
    painter->drawPixmap(0, 0, pixmap);
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalfocusrectangle.cpp, line 14, as _ZN29QQuickUniversalFocusRectangleC1EP10QQuickItem
inline QQuickUniversalFocusRectangle::QQuickUniversalFocusRectangle(QQuickItem *parent)
    : QQuickPaintedItem(parent)
{
    QQuickItemPrivate::get(this)->setTransparentForPositioner(true);
}
//  -----------------------------------------------------------------------

//  A QQuickUniversalFocusRectangle that Python can take functions over in. Every QQuickUniversalFocusRectangle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickUniversalFocusRectangleCall0)(const void *, QPainter *, int *);
typedef bool (*CuteQQuickUniversalFocusRectangleCall1)(const void *, int *);
typedef void * (*CuteQQuickUniversalFocusRectangleCall2)(const void *, int *);
typedef void * (*CuteQQuickUniversalFocusRectangleCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall4)(const void *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall5)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef const QRectF * (*CuteQQuickUniversalFocusRectangleCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickUniversalFocusRectangleCall7)(const void *, int *);
typedef bool (*CuteQQuickUniversalFocusRectangleCall8)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickUniversalFocusRectangleCall9)(const void *, int, int *);
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickUniversalFocusRectangleCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniversalFocusRectangleCall11)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall12)(const void *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall13)(const void *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall14)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall15)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickUniversalFocusRectangleCall16)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickUniversalFocusRectangleCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall23)(const void *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall24)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickUniversalFocusRectangleCall25)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickUniversalFocusRectangleCall26)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall29)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickUniversalFocusRectangleCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickUniversalFocusRectangleCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickUniversalFocusRectangleCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickUniversalFocusRectangleCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickUniversalFocusRectangleCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickUniversalFocusRectangleCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickUniversalFocusRectangleCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniversalFocusRectangleCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniversalFocusRectangleCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniversalFocusRectangleCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniversalFocusRectangleCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickUniversalFocusRectangleCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickUniversalFocusRectangle : public QQuickUniversalFocusRectangle {
public:
  using QQuickUniversalFocusRectangle::QQuickUniversalFocusRectangle;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickPaintedItem5paintEP8QPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[24] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickUniversalFocusRectangle::paint(QPainter *painter)
  void paint(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall0 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QQuickUniversalFocusRectangle::paint(painter);
  }

  //  bool QQuickPaintedItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall1 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPaintedItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickPaintedItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall2 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickPaintedItem::textureProvider();
  }

  //  QSGNode *QQuickPaintedItem::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall3 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickPaintedItem::updatePaintNode(a0, a1);
  }

  //  void QQuickPaintedItem::releaseResources()
  void releaseResources() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall4 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::releaseResources();
  }

  //  void QQuickPaintedItem::itemChange(ItemChange a0, const
  //      ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall5 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickPaintedItem::itemChange(a0, a1);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall6 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall7 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall8 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall8>(taken[8]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall9 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall10 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall11 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall11>(taken[11]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall12 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall13 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall14 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall15 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall16 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall17 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall18 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall19 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall20 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall21 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall22 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall23 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall24 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall25 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall26 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall27 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall28 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall29 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall30 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall31 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall32 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall33 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall34 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall35 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall36 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall37 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall38 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall39 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall40 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickUniversalFocusRectangleCall41 call = reinterpret_cast<CuteQQuickUniversalFocusRectangleCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickUniversalFocusRectangle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickUniversalFocusRectangle10metaObjectEv(
    const QQuickUniversalFocusRectangle *self) {
  return self->metaObject();
}

//  void *QQuickUniversalFocusRectangle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuickUniversalFocusRectangle11qt_metacastEPKc(
    QQuickUniversalFocusRectangle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickUniversalFocusRectangle::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuickUniversalFocusRectangle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickUniversalFocusRectangle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickUniversalFocusRectangle::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickUniversalFocusRectangle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickUniversalFocusRectangle::tr(s, c, n));
}

//  QQuickUniversalFocusRectangle::QQuickUniversalFocusRectangle(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickUniversalFocusRectangle *ritual_ZN29QQuickUniversalFocusRectangleC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickUniversalFocusRectangle(parent);
}

//  void QQuickUniversalFocusRectangle::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickUniversalFocusRectangle5paintEP8QPainter(
    QQuickUniversalFocusRectangle *self,
    QPainter *painter) {
  self->paint(painter);
}

//  a Python function taken by a CuteQQuickUniversalFocusRectangle, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickUniversalFocusRectangle(
    QQuickUniversalFocusRectangle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickUniversalFocusRectangle *>(self)->take(key, call);
}

//  void QQuickUniversalFocusRectangle::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickUniversalFocusRectangle5paintEP8QPainter(
    QQuickUniversalFocusRectangle *self,
    QPainter *painter) {
  self->QQuickUniversalFocusRectangle::paint(painter);
}
