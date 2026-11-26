//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/areaallocator_p.h>
#include <QtCore/qglobal.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <Qt3DExtras/private/qtextureatlas_p.h>
#include <Qt3DExtras/private/qtextureatlas_p_p.h>
#include <Qt3DRender/qtexturedata.h>
#include <Qt3DRender/qabstracttextureimage.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 18, as local:areaallocator.cpp:SplitType
namespace Qt3DExtras {
enum SplitType
{
    VerticalSplit,
    HorizontalSplit
};
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 24, as local:areaallocator.cpp:maxMargin
namespace Qt3DExtras {
static const int maxMargin = 2;
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 26, as local:areaallocator.cpp:AreaAllocatorNode
namespace Qt3DExtras {
struct AreaAllocatorNode
{
    AreaAllocatorNode(AreaAllocatorNode *parent);
    ~AreaAllocatorNode();
    inline bool isLeaf();

    AreaAllocatorNode *parent;
    AreaAllocatorNode *left;
    AreaAllocatorNode *right;
    int split; // only valid for inner nodes.
    SplitType splitType;
    bool isOccupied; // only valid for leaf nodes.
};
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 40, as local:areaallocator.cpp:AreaAllocatorNode::AreaAllocatorNode
namespace Qt3DExtras {
inline AreaAllocatorNode::AreaAllocatorNode(AreaAllocatorNode *parent)
    : parent(parent)
    , left(0)
    , right(0)
    , isOccupied(false)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 48, as local:areaallocator.cpp:AreaAllocatorNode::~AreaAllocatorNode
namespace Qt3DExtras {
inline AreaAllocatorNode::~AreaAllocatorNode()
{
    delete left;
    delete right;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 54, as local:areaallocator.cpp:AreaAllocatorNode::isLeaf
namespace Qt3DExtras {
inline bool AreaAllocatorNode::isLeaf()
{
    Q_ASSERT((left != 0) == (right != 0));
    return !left;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 71, as _ZN10Qt3DExtras13AreaAllocator8allocateERK5QSize
namespace Qt3DExtras {
inline QRect AreaAllocator::allocate(const QSize &size)
{
    QPoint point;
    bool result = allocateInNode(size, point, QRect(QPoint(0, 0), m_size), m_root);
    return result ? QRect(point, size) : QRect();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 61, as _ZN10Qt3DExtras13AreaAllocatorC1ERK5QSize
namespace Qt3DExtras {
inline AreaAllocator::AreaAllocator(const QSize &size) : m_size(size)
{
    m_root = new AreaAllocatorNode(0);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 66, as _ZN10Qt3DExtras13AreaAllocatorD1Ev
namespace Qt3DExtras {
inline AreaAllocator::~AreaAllocator()
{
    delete m_root;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 26, as _ZN10Qt3DExtras17QTextureAtlasData8addImageERKNS_12AtlasTextureERK6QImage
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QTextureAtlasData::addImage(const AtlasTexture &texture, const QImage &image)
{
    QMutexLocker lock(&m_mutex);

    Update update;
    update.textureInfo = texture;
    update.image = image;
    m_updates << update;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 16, as _ZN10Qt3DExtras17QTextureAtlasDataC1EiiN6QImage6FormatE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasData::QTextureAtlasData(int w, int h, QImage::Format fmt)
    : m_image(w, h, fmt)
{
    m_image.fill(0);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 22, as _ZN10Qt3DExtras17QTextureAtlasDataD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasData::~QTextureAtlasData()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 99, as _ZN10Qt3DExtras22QTextureAtlasGeneratorC1EPKNS_20QTextureAtlasPrivateE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasGenerator::QTextureAtlasGenerator(const QTextureAtlasPrivate *texAtlas)
    : m_data(texAtlas->m_data)
    , m_format(texAtlas->m_format)
    , m_pixelFormat(texAtlas->m_pixelFormat)
    , m_generation(texAtlas->m_currGen)
    , m_atlasId(texAtlas->m_id)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 108, as _ZN10Qt3DExtras22QTextureAtlasGeneratorD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasGenerator::~QTextureAtlasGenerator()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 78, as _ZN10Qt3DExtras13AreaAllocator10deallocateERK5QRect
namespace Qt3DExtras {
inline bool AreaAllocator::deallocate(const QRect &rect)
{
    return deallocateInNode(rect.topLeft(), m_root);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 83, as _ZN10Qt3DExtras13AreaAllocator14allocateInNodeERK5QSizeR6QPointRK5QRectPNS_17AreaAllocatorNodeE
namespace Qt3DExtras {
inline bool AreaAllocator::allocateInNode(const QSize &size, QPoint &result, const QRect &currentRect, AreaAllocatorNode *node)
{
    if (size.width() > currentRect.width() || size.height() > currentRect.height())
        return false;

    if (node->isLeaf()) {
        if (node->isOccupied)
            return false;
        if (size.width() + maxMargin >= currentRect.width() && size.height() + maxMargin >= currentRect.height()) {
            //Snug fit, occupy entire rectangle.
            node->isOccupied = true;
            result = currentRect.topLeft();
            return true;
        }
        // TODO: Reuse nodes.
        // Split node.
        node->left = new AreaAllocatorNode(node);
        node->right = new AreaAllocatorNode(node);
        QRect splitRect = currentRect;
        if ((currentRect.width() - size.width()) * currentRect.height() < (currentRect.height() - size.height()) * currentRect.width()) {
            node->splitType = HorizontalSplit;
            node->split = currentRect.top() + size.height();
            splitRect.setHeight(size.height());
        } else {
            node->splitType = VerticalSplit;
            node->split = currentRect.left() + size.width();
            splitRect.setWidth(size.width());
        }
        return allocateInNode(size, result, splitRect, node->left);
    } else {
        // TODO: avoid unnecessary recursion.
        //  has been split.
        QRect leftRect = currentRect;
        QRect rightRect = currentRect;
        if (node->splitType == HorizontalSplit) {
            leftRect.setHeight(node->split - leftRect.top());
            rightRect.setTop(node->split);
        } else {
            leftRect.setWidth(node->split - leftRect.left());
            rightRect.setLeft(node->split);
        }
        if (allocateInNode(size, result, leftRect, node->left))
            return true;
        if (allocateInNode(size, result, rightRect, node->right))
            return true;
        return false;
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 132, as _ZN10Qt3DExtras13AreaAllocator16deallocateInNodeERK6QPointPNS_17AreaAllocatorNodeE
namespace Qt3DExtras {
inline bool AreaAllocator::deallocateInNode(const QPoint &pos, AreaAllocatorNode *node)
{
    while (!node->isLeaf()) {
        //  has been split.
        int cmp = node->splitType == HorizontalSplit ? pos.y() : pos.x();
        node = cmp < node->split ? node->left : node->right;
    }
    if (!node->isOccupied)
        return false;
    node->isOccupied = false;
    mergeNodeWithNeighbors(node);
    return true;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 146, as _ZN10Qt3DExtras13AreaAllocator22mergeNodeWithNeighborsEPNS_17AreaAllocatorNodeE
namespace Qt3DExtras {
inline void AreaAllocator::mergeNodeWithNeighbors(AreaAllocatorNode *node)
{
    bool done = false;
    AreaAllocatorNode *parent = 0;
    AreaAllocatorNode *current = 0;
    AreaAllocatorNode *sibling;
    while (!done) {
        Q_ASSERT(node->isLeaf());
        Q_ASSERT(!node->isOccupied);
        if (node->parent == 0)
            return; // No neighbors.

        SplitType splitType = SplitType(node->parent->splitType);
        done = true;

        /* Special case. Might be faster than going through the general code path.
        // Merge with sibling.
        parent = node->parent;
        sibling = (node == parent->left ? parent->right : parent->left);
        if (sibling->isLeaf() && !sibling->isOccupied) {
            Q_ASSERT(!sibling->right);
            node = parent;
            parent->isOccupied = false;
            delete parent->left;
            delete parent->right;
            parent->left = parent->right = 0;
            done = false;
            continue;
        }
        */

        // Merge with left neighbor.
        current = node;
        parent = current->parent;
        while (parent && current == parent->left && parent->splitType == splitType) {
            current = parent;
            parent = parent->parent;
        }

        if (parent && parent->splitType == splitType) {
            Q_ASSERT(current == parent->right);
            Q_ASSERT(parent->left);

            AreaAllocatorNode *neighbor = parent->left;
            while (neighbor->right && neighbor->splitType == splitType)
                neighbor = neighbor->right;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType && !neighbor->isOccupied) {
                // Left neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                AreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = 0;
                delete parent;
                delete neighbor;
                done = false;
            }
        }

        // Merge with right neighbor.
        current = node;
        parent = current->parent;
        while (parent && current == parent->right && parent->splitType == splitType) {
            current = parent;
            parent = parent->parent;
        }

        if (parent && parent->splitType == splitType) {
            Q_ASSERT(current == parent->left);
            Q_ASSERT(parent->right);

            AreaAllocatorNode *neighbor = parent->right;
            while (neighbor->left && neighbor->splitType == splitType)
                neighbor = neighbor->left;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType && !neighbor->isOccupied) {
                // Right neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                AreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = 0;
                delete parent;
                delete neighbor;
                done = false;
            }
        }
    } // end while (!done)
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 167, as _ZN10Qt3DExtras13QTextureAtlasD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlas::~QTextureAtlas()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 155, as _ZNK10Qt3DExtras13QTextureAtlas11pixelFormatEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QOpenGLTexture::PixelFormat QTextureAtlas::pixelFormat() const
{
    Q_D(const QTextureAtlas);
    return d->m_pixelFormat;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 161, as _ZN10Qt3DExtras13QTextureAtlas14setPixelFormatEN14QOpenGLTexture11PixelFormatE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QTextureAtlas::setPixelFormat(QOpenGLTexture::PixelFormat fmt)
{
    Q_D(QTextureAtlas);
    d->m_pixelFormat = fmt;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 207, as _ZN10Qt3DExtras13QTextureAtlas11removeImageEi
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QTextureAtlas::removeImage(TextureId id)
{
    Q_D(QTextureAtlas);
    auto it = d->m_textures.find(id);
    if (it != d->m_textures.end()) {
        QRect imgRect = it->position;
        imgRect.adjust(-it->padding, -it->padding, 2*it->padding, 2*it->padding);

        if (d->m_allocator)
            d->m_allocator->deallocate(imgRect);
        d->m_textures.erase(it);
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 227, as _ZNK10Qt3DExtras13QTextureAtlas10imageCountEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline qsizetype QTextureAtlas::imageCount() const
{
    Q_D(const QTextureAtlas);
    return d->m_textures.size();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 221, as _ZNK10Qt3DExtras13QTextureAtlas8hasImageEi
namespace Qt3DExtras {
using namespace Qt3DCore;
inline bool QTextureAtlas::hasImage(TextureId id) const
{
    Q_D(const QTextureAtlas);
    return d->m_textures.contains(id);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 233, as _ZNK10Qt3DExtras13QTextureAtlas13imagePositionEi
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QRect QTextureAtlas::imagePosition(TextureId id) const
{
    Q_D(const QTextureAtlas);
    const auto it = d->m_textures.find(id);
    return (it != d->m_textures.cend()) ? it->position : QRect();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 240, as _ZNK10Qt3DExtras13QTextureAtlas14imageTexCoordsEi
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QRectF QTextureAtlas::imageTexCoords(TextureId id) const
{
    Q_D(const QTextureAtlas);
    const auto it = d->m_textures.find(id);
    if (it != d->m_textures.cend()) {
        const float w = d->m_data->width();
        const float h = d->m_data->height();
        return QRectF(static_cast<float>(it->position.x()) / w,
                      static_cast<float>(it->position.y()) / h,
                      static_cast<float>(it->position.width()) / w,
                      static_cast<float>(it->position.height()) / h);
    }
    return QRectF();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 255, as _ZNK10Qt3DExtras13QTextureAtlas12imagePaddingEi
namespace Qt3DExtras {
using namespace Qt3DCore;
inline int QTextureAtlas::imagePadding(TextureId id) const
{
    Q_D(const QTextureAtlas);
    const auto it = d->m_textures.find(id);
    return (it != d->m_textures.cend()) ? it->padding : -1;
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QTextureAtlas that Python can take functions over in. Every Qt3DExtras::QTextureAtlas
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTextureAtlasCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QTextureAtlasCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureAtlasCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureAtlasCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureAtlasCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureAtlasCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QTextureAtlasCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QTextureAtlas : public Qt3DExtras::QTextureAtlas {
public:
  using Qt3DExtras::QTextureAtlas::QTextureAtlas;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall0 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall1 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall2 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall3 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall4 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall5 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasCall6 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QTextureAtlas::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras13QTextureAtlas10metaObjectEv(
    const Qt3DExtras::QTextureAtlas *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QTextureAtlas::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras13QTextureAtlas11qt_metacastEPKc(
    Qt3DExtras::QTextureAtlas *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QTextureAtlas::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras13QTextureAtlas11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QTextureAtlas *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DExtras::QTextureAtlas::~QTextureAtlas()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QTextureAtlasD1Ev(
    Qt3DExtras::QTextureAtlas *self) {
  delete self;
}

//  QOpenGLTexture::PixelFormat Qt3DExtras::QTextureAtlas::pixelFormat()
//      const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::PixelFormat ritual_ZNK10Qt3DExtras13QTextureAtlas11pixelFormatEv(
    const Qt3DExtras::QTextureAtlas *self) {
  return self->pixelFormat();
}

//  void
//      Qt3DExtras::QTextureAtlas::setPixelFormat(QOpenGLTexture::PixelFormat
//      fmt)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QTextureAtlas14setPixelFormatEN14QOpenGLTexture11PixelFormatE(
    Qt3DExtras::QTextureAtlas *self,
    QOpenGLTexture::PixelFormat fmt) {
  self->setPixelFormat(fmt);
}

//  void Qt3DExtras::QTextureAtlas::removeImage(TextureId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QTextureAtlas11removeImageEi(
    Qt3DExtras::QTextureAtlas *self,
    Qt3DExtras::QTextureAtlas::TextureId id) {
  self->removeImage(id);
}

//  qsizetype Qt3DExtras::QTextureAtlas::imageCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10Qt3DExtras13QTextureAtlas10imageCountEv(
    const Qt3DExtras::QTextureAtlas *self) {
  return self->imageCount();
}

//  bool Qt3DExtras::QTextureAtlas::hasImage(TextureId id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras13QTextureAtlas8hasImageEi(
    const Qt3DExtras::QTextureAtlas *self,
    Qt3DExtras::QTextureAtlas::TextureId id) {
  return self->hasImage(id);
}

//  QRect Qt3DExtras::QTextureAtlas::imagePosition(TextureId id) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10Qt3DExtras13QTextureAtlas13imagePositionEi(
    const Qt3DExtras::QTextureAtlas *self,
    Qt3DExtras::QTextureAtlas::TextureId id) {
  return new QRect(self->imagePosition(id));
}

//  QRectF Qt3DExtras::QTextureAtlas::imageTexCoords(TextureId id) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DExtras13QTextureAtlas14imageTexCoordsEi(
    const Qt3DExtras::QTextureAtlas *self,
    Qt3DExtras::QTextureAtlas::TextureId id) {
  return new QRectF(self->imageTexCoords(id));
}

//  int Qt3DExtras::QTextureAtlas::imagePadding(TextureId id) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras13QTextureAtlas12imagePaddingEi(
    const Qt3DExtras::QTextureAtlas *self,
    Qt3DExtras::QTextureAtlas::TextureId id) {
  return self->imagePadding(id);
}

//  QTextureAtlasPrivate *Qt3DExtras::QTextureAtlas::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureAtlasPrivate *ritual_ZN10Qt3DExtras13QTextureAtlas6d_funcEv(
    Qt3DExtras::QTextureAtlas *self) {
  return self->d_func();
}

//  const QTextureAtlasPrivate *Qt3DExtras::QTextureAtlas::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QTextureAtlasPrivate *ritual_ZNK10Qt3DExtras13QTextureAtlas6d_funcEv(
    const Qt3DExtras::QTextureAtlas *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QTextureAtlas, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTextureAtlas(
    Qt3DExtras::QTextureAtlas *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTextureAtlas *>(self)->take(key, call);
}
