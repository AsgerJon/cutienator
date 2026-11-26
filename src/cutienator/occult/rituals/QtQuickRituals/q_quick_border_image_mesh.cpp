//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQuickBorderImageMesh' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 5 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuick/private/qquickshadereffectmesh_p.h>
#include <QtQuick/qsggeometry.h>
#include <QtQuick/private/qquickshadereffect_p.h>
#include <QtQuick/private/qquickscalegrid_p_p.h>
#include <QtQuick/private/qquickborderimage_p_p.h>
#include <QtQuick/private/qsgbasicinternalimagenode_p.h>
#include <QtQuick/private/qquickborderimage_p.h>
#include <QtQuick/private/qquickborderimage_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlengine.h>
#if QT_CONFIG(qml_network)
#include <QtNetwork/qnetworkreply.h>
#endif
#include <QtCore/qfile.h>
#include <QtCore/qmath.h>
#include <QtGui/qguiapplication.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQuick__QQuickBorderImageMesh.cpp, line 1, as moc:QQuickBorderImageMesh
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN21QQuickBorderImageMeshE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickBorderImageMesh::qt_create_metaobjectdata<qt_meta_tag_ZN21QQuickBorderImageMeshE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickBorderImageMesh",
        "QML.Element",
        "BorderImageMesh",
        "QML.AddedInVersion",
        "520",
        "sizeChanged",
        "",
        "horizontalTileModeChanged",
        "verticalTileModeChanged",
        "border",
        "QQuickScaleGrid*",
        "size",
        "QSize",
        "horizontalTileMode",
        "TileMode",
        "verticalTileMode",
        "Stretch",
        "Repeat",
        "Round"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'sizeChanged'
        QtMocHelpers::SignalData<void()>(5, 6, QMC::AccessPublic, QMetaType::Void),
        // Signal 'horizontalTileModeChanged'
        QtMocHelpers::SignalData<void()>(7, 6, QMC::AccessPublic, QMetaType::Void),
        // Signal 'verticalTileModeChanged'
        QtMocHelpers::SignalData<void()>(8, 6, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'border'
        QtMocHelpers::PropertyData<QQuickScaleGrid*>(9, 0x80000000 | 10, QMC::DefaultPropertyFlags | QMC::EnumOrFlag | QMC::Constant),
        // property 'size'
        QtMocHelpers::PropertyData<QSize>(11, 0x80000000 | 12, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 0),
        // property 'horizontalTileMode'
        QtMocHelpers::PropertyData<enum TileMode>(13, 0x80000000 | 14, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 1),
        // property 'verticalTileMode'
        QtMocHelpers::PropertyData<enum TileMode>(15, 0x80000000 | 14, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 2),
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'TileMode'
        QtMocHelpers::EnumData<enum TileMode>(14, 14, QMC::EnumFlags{}).add({
            {   16, TileMode::Stretch },
            {   17, TileMode::Repeat },
            {   18, TileMode::Round },
        }),
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<QQuickBorderImageMesh, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QQuickBorderImageMesh::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickShaderEffectMesh::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQuickBorderImageMeshE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQuickBorderImageMeshE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN21QQuickBorderImageMeshE_t>.metaTypes,
    nullptr
} };

void QQuickBorderImageMesh::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickBorderImageMesh *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->sizeChanged(); break;
        case 1: _t->horizontalTileModeChanged(); break;
        case 2: _t->verticalTileModeChanged(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQuickBorderImageMesh::*)()>(_a, &QQuickBorderImageMesh::sizeChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickBorderImageMesh::*)()>(_a, &QQuickBorderImageMesh::horizontalTileModeChanged, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQuickBorderImageMesh::*)()>(_a, &QQuickBorderImageMesh::verticalTileModeChanged, 2))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QQuickScaleGrid**>(_v) = _t->border(); break;
        case 1: *reinterpret_cast<QSize*>(_v) = _t->size(); break;
        case 2: *reinterpret_cast<enum TileMode*>(_v) = _t->horizontalTileMode(); break;
        case 3: *reinterpret_cast<enum TileMode*>(_v) = _t->verticalTileMode(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setSize(*reinterpret_cast<QSize*>(_v)); break;
        case 2: _t->setHorizontalTileMode(*reinterpret_cast<enum TileMode*>(_v)); break;
        case 3: _t->setVerticalTileMode(*reinterpret_cast<enum TileMode*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQuickBorderImageMesh::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickBorderImageMesh::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QQuickBorderImageMeshE_t>.strings))
        return static_cast<void*>(this);
    return QQuickShaderEffectMesh::qt_metacast(_clname);
}

int QQuickBorderImageMesh::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickShaderEffectMesh::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void QQuickBorderImageMesh::sizeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQuickBorderImageMesh::horizontalTileModeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void QQuickBorderImageMesh::verticalTileModeChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 296, as _ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_
inline QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry, int attrCount, int posIndex,
                                                   const QRectF &srcRect, const QRectF &rect)
{
    Q_UNUSED(attrCount);
    Q_UNUSED(posIndex);

    QRectF innerSourceRect;
    QRectF targetRect;
    QRectF innerTargetRect;
    QRectF subSourceRect;

    QQuickBorderImagePrivate::calculateRects(m_border, m_size, rect.size(), m_horizontalTileMode, m_verticalTileMode,
                                             1, &targetRect, &innerTargetRect, &innerSourceRect, &subSourceRect);

    QRectF sourceRect = srcRect;
    QRectF modifiedInnerSourceRect(sourceRect.x() + innerSourceRect.x() * sourceRect.width(),
                                   sourceRect.y() + innerSourceRect.y() * sourceRect.height(),
                                   innerSourceRect.width() * sourceRect.width(),
                                   innerSourceRect.height() * sourceRect.height());

    geometry = QSGBasicInternalImageNode::updateGeometry(targetRect, innerTargetRect, sourceRect,
                                                         modifiedInnerSourceRect, subSourceRect, geometry);

    return geometry;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 289, as _ZN21QQuickBorderImageMesh18validateAttributesERK5QListI10QByteArrayEPi
inline bool QQuickBorderImageMesh::validateAttributes(const QList<QByteArray> &attributes, int *posIndex)
{
    Q_UNUSED(attributes);
    Q_UNUSED(posIndex);
    return true;
}

//  from ../qtdeclarative/src/quick/items/qquickborderimage.cpp, line 465, as _ZN24QQuickBorderImagePrivate14calculateRectsEPK15QQuickScaleGridRK5QSizeRK6QSizeFiidP6QRectFSA_SA_SA_
inline void QQuickBorderImagePrivate::calculateRects(const QQuickScaleGrid *border,
                                              const QSize &sourceSize,
                                              const QSizeF &targetSize,
                                              int horizontalTileMode,
                                              int verticalTileMode,
                                              qreal devicePixelRatio,
                                              QRectF *targetRect,
                                              QRectF *innerTargetRect,
                                              QRectF *innerSourceRect,
                                              QRectF *subSourceRect)
{
    *innerSourceRect = QRectF(0, 0, 1, 1);
    *targetRect = QRectF(0, 0, targetSize.width(), targetSize.height());
    *innerTargetRect = *targetRect;

    if (border) {
        qreal borderLeft = border->left() * devicePixelRatio;
        qreal borderRight = border->right() * devicePixelRatio;
        qreal borderTop = border->top() * devicePixelRatio;
        qreal borderBottom = border->bottom() * devicePixelRatio;
        if (borderLeft + borderRight > sourceSize.width() && borderLeft < sourceSize.width())
            borderRight = sourceSize.width() - borderLeft;
        if (borderTop + borderBottom > sourceSize.height() && borderTop < sourceSize.height())
            borderBottom = sourceSize.height() - borderTop;
        *innerSourceRect = QRectF(QPointF(borderLeft / qreal(sourceSize.width()),
                                          borderTop / qreal(sourceSize.height())),
                                  QPointF((sourceSize.width() - borderRight) / qreal(sourceSize.width()),
                                          (sourceSize.height() - borderBottom) / qreal(sourceSize.height()))),
        *innerTargetRect = QRectF(border->left(),
                                  border->top(),
                                  qMax<qreal>(0, targetSize.width() - (border->right() + border->left())),
                                  qMax<qreal>(0, targetSize.height() - (border->bottom() + border->top())));
    }

    qreal hTiles = 1;
    qreal vTiles = 1;
    const QSizeF innerTargetSize = innerTargetRect->size() * devicePixelRatio;
    if (innerSourceRect->width() <= 0)
        hTiles = 0;
    else if (horizontalTileMode != QQuickBorderImage::Stretch) {
        hTiles = innerTargetSize.width() / qreal(innerSourceRect->width() * sourceSize.width());
        if (horizontalTileMode == QQuickBorderImage::Round)
            hTiles = qCeil(hTiles);
    }
    if (innerSourceRect->height() <= 0)
        vTiles = 0;
    else if (verticalTileMode != QQuickBorderImage::Stretch) {
        vTiles = innerTargetSize.height() / qreal(innerSourceRect->height() * sourceSize.height());
        if (verticalTileMode == QQuickBorderImage::Round)
            vTiles = qCeil(vTiles);
    }

    *subSourceRect = QRectF(0, 0, hTiles, vTiles);
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 282, as _ZN21QQuickBorderImageMeshC1EP7QObject
inline QQuickBorderImageMesh::QQuickBorderImageMesh(QObject *parent)
    : QQuickShaderEffectMesh(parent), m_border(new QQuickScaleGrid(this)),
      m_horizontalTileMode(QQuickBorderImageMesh::Stretch),
      m_verticalTileMode(QQuickBorderImageMesh::Stretch)
{
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 349, as _ZNK21QQuickBorderImageMesh6borderEv
inline QQuickScaleGrid *QQuickBorderImageMesh::border() const
{
    return m_border;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 360, as _ZNK21QQuickBorderImageMesh4sizeEv
inline QSize QQuickBorderImageMesh::size() const
{
    return m_size;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 365, as _ZN21QQuickBorderImageMesh7setSizeERK5QSize
inline void QQuickBorderImageMesh::setSize(const QSize &size)
{
    if (size == m_size)
        return;
    m_size = size;
    Q_EMIT sizeChanged();
    Q_EMIT geometryChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 389, as _ZNK21QQuickBorderImageMesh18horizontalTileModeEv
inline QQuickBorderImageMesh::TileMode QQuickBorderImageMesh::horizontalTileMode() const
{
    return m_horizontalTileMode;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 394, as _ZN21QQuickBorderImageMesh21setHorizontalTileModeENS_8TileModeE
inline void QQuickBorderImageMesh::setHorizontalTileMode(TileMode t)
{
    if (t == m_horizontalTileMode)
        return;
    m_horizontalTileMode = t;
    Q_EMIT horizontalTileModeChanged();
    Q_EMIT geometryChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 403, as _ZNK21QQuickBorderImageMesh16verticalTileModeEv
inline QQuickBorderImageMesh::TileMode QQuickBorderImageMesh::verticalTileMode() const
{
    return m_verticalTileMode;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 408, as _ZN21QQuickBorderImageMesh19setVerticalTileModeENS_8TileModeE
inline void QQuickBorderImageMesh::setVerticalTileMode(TileMode t)
{
    if (t == m_verticalTileMode)
        return;

    m_verticalTileMode = t;
    Q_EMIT verticalTileModeChanged();
    Q_EMIT geometryChanged();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickBorderImageMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickBorderImageMesh10metaObjectEv(
    const QQuickBorderImageMesh *self) {
  return self->metaObject();
}

//  void *QQuickBorderImageMesh::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickBorderImageMesh11qt_metacastEPKc(
    QQuickBorderImageMesh *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBorderImageMesh::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickBorderImageMesh11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBorderImageMesh *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickBorderImageMesh::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickBorderImageMesh2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickBorderImageMesh::tr(s, c, n));
}

//  QQuickBorderImageMesh::QQuickBorderImageMesh(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickBorderImageMesh *ritual_ZN21QQuickBorderImageMeshC1EP7QObject(
    QObject *parent) {
  return new QQuickBorderImageMesh(parent);
}

//  bool QQuickBorderImageMesh::validateAttributes(const QList<QByteArray>
//      &attributes, int *posIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickBorderImageMesh18validateAttributesERK5QListI10QByteArrayEPi(
    QQuickBorderImageMesh *self,
    const QList<QByteArray> *attributes,
    int *posIndex) {
  return self->validateAttributes(*attributes, posIndex);
}

//  QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry,
//      int attrCount, int posIndex, const QRectF &srcRect, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickBorderImageMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

//  QQuickScaleGrid *QQuickBorderImageMesh::border() const
extern "C" Q_DECL_EXPORT
QQuickScaleGrid *ritual_ZNK21QQuickBorderImageMesh6borderEv(
    const QQuickBorderImageMesh *self) {
  return self->border();
}

//  QSize QQuickBorderImageMesh::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QQuickBorderImageMesh4sizeEv(
    const QQuickBorderImageMesh *self) {
  return new QSize(self->size());
}

//  void QQuickBorderImageMesh::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickBorderImageMesh7setSizeERK5QSize(
    QQuickBorderImageMesh *self,
    const QSize *size) {
  self->setSize(*size);
}

//  TileMode QQuickBorderImageMesh::horizontalTileMode() const
extern "C" Q_DECL_EXPORT
QQuickBorderImageMesh::TileMode ritual_ZNK21QQuickBorderImageMesh18horizontalTileModeEv(
    const QQuickBorderImageMesh *self) {
  return self->horizontalTileMode();
}

//  void QQuickBorderImageMesh::setHorizontalTileMode(TileMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickBorderImageMesh21setHorizontalTileModeENS_8TileModeE(
    QQuickBorderImageMesh *self,
    QQuickBorderImageMesh::TileMode a0) {
  self->setHorizontalTileMode(a0);
}

//  TileMode QQuickBorderImageMesh::verticalTileMode() const
extern "C" Q_DECL_EXPORT
QQuickBorderImageMesh::TileMode ritual_ZNK21QQuickBorderImageMesh16verticalTileModeEv(
    const QQuickBorderImageMesh *self) {
  return self->verticalTileMode();
}

//  void QQuickBorderImageMesh::setVerticalTileMode(TileMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickBorderImageMesh19setVerticalTileModeENS_8TileModeE(
    QQuickBorderImageMesh *self,
    QQuickBorderImageMesh::TileMode a0) {
  self->setVerticalTileMode(a0);
}

//  void QQuickBorderImageMesh::sizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickBorderImageMesh11sizeChangedEv(
    QQuickBorderImageMesh *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickBorderImageMesh")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickBorderImageMesh::horizontalTileModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickBorderImageMesh25horizontalTileModeChangedEv(
    QQuickBorderImageMesh *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickBorderImageMesh")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "horizontalTileModeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "horizontalTileModeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickBorderImageMesh::verticalTileModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickBorderImageMesh23verticalTileModeChangedEv(
    QQuickBorderImageMesh *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickBorderImageMesh")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "verticalTileModeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "verticalTileModeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry,
//      int attrCount, int posIndex, const QRectF &srcRect, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_own_ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickBorderImageMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->QQuickBorderImageMesh::updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

#endif  // QT_CONFIG(quick_shadereffect)
#endif  // QT_CONFIG(quick_shadereffect)
