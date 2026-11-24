//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgnode_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgnode_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSvgNode that Python can take functions over in. Every QSvgNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgNodeCall0)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgNodeCall1)(const void *, int *);
typedef bool (*CuteQSvgNodeCall2)(const void *, int *);
class CuteQSvgNode : public QSvgNode {
public:
  using QSvgNode::QSvgNode;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgNodeCall0 call = reinterpret_cast<CuteQSvgNodeCall0>(taken[0]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  Type QSvgNode::type() const
  QSvgNode::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgNodeCall1 call = reinterpret_cast<CuteQSvgNodeCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return {};
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgNodeCall2 call = reinterpret_cast<CuteQSvgNodeCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgNode::~QSvgNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNodeD1Ev(QSvgNode *self) {
  delete self;
}

//  bool QSvgNode::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgNode *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  void QSvgNode::applyMaskToBuffer(QImage *proxy, const QImage &mask) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QSvgNode17applyMaskToBufferEP6QImageRKS0_(
    const QSvgNode *self,
    QImage *proxy,
    const QImage *mask) {
  self->applyMaskToBuffer(proxy, *mask);
}

//  void QSvgNode::applyBufferToCanvas(QPainter *p, const QImage &proxy)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QSvgNode19applyBufferToCanvasEP8QPainterRK6QImage(
    const QSvgNode *self,
    QPainter *p,
    const QImage *proxy) {
  self->applyBufferToCanvas(p, *proxy);
}

//  QSvgNode *QSvgNode::parent() const
extern "C" Q_DECL_EXPORT
QSvgNode *ritual_ZNK8QSvgNode6parentEv(const QSvgNode *self) {
  return self->parent();
}

//  bool QSvgNode::isDescendantOf(const QSvgNode *parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode14isDescendantOfEPKS_(
    const QSvgNode *self,
    const QSvgNode *parent) {
  return self->isDescendantOf(parent);
}

//  QSvgStyleProperty *QSvgNode::styleProperty(QSvgStyleProperty::Type type)
//      const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty *ritual_ZNK8QSvgNode13stylePropertyEN17QSvgStyleProperty4TypeE(
    const QSvgNode *self,
    QSvgStyleProperty::Type type) {
  return self->styleProperty(type);
}

//  QSvgDocument *QSvgNode::document() const
extern "C" Q_DECL_EXPORT
QSvgDocument *ritual_ZNK8QSvgNode8documentEv(const QSvgNode *self) {
  return self->document();
}

//  Type QSvgNode::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgNode4typeEv(const QSvgNode *self) {
  return self->type();
}

//  QLatin1StringView QSvgNode::typeName() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK8QSvgNode8typeNameEv(const QSvgNode *self) {
  return new QLatin1String(self->typeName());
}

//  QRectF QSvgNode::bounds(const QSvgDocument *doc) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QSvgNode6boundsEPK12QSvgDocument(
    const QSvgNode *self,
    const QSvgDocument *doc) {
  return new QRectF(self->bounds(doc));
}

//  void QSvgNode::setRequiredFeatures(const QStringList &lst)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode19setRequiredFeaturesERK5QListI7QStringE(
    QSvgNode *self,
    const QList<QString> *lst) {
  self->setRequiredFeatures(*lst);
}

//  const QStringList &QSvgNode::requiredFeatures() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QSvgNode16requiredFeaturesEv(
    const QSvgNode *self) {
  return new QList<QString>(self->requiredFeatures());
}

//  void QSvgNode::setRequiredExtensions(const QStringList &lst)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode21setRequiredExtensionsERK5QListI7QStringE(
    QSvgNode *self,
    const QList<QString> *lst) {
  self->setRequiredExtensions(*lst);
}

//  const QStringList &QSvgNode::requiredExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QSvgNode18requiredExtensionsEv(
    const QSvgNode *self) {
  return new QList<QString>(self->requiredExtensions());
}

//  void QSvgNode::setRequiredLanguages(const QStringList &lst)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode20setRequiredLanguagesERK5QListI7QStringE(
    QSvgNode *self,
    const QList<QString> *lst) {
  self->setRequiredLanguages(*lst);
}

//  const QStringList &QSvgNode::requiredLanguages() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QSvgNode17requiredLanguagesEv(
    const QSvgNode *self) {
  return new QList<QString>(self->requiredLanguages());
}

//  void QSvgNode::setRequiredFormats(const QStringList &lst)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode18setRequiredFormatsERK5QListI7QStringE(
    QSvgNode *self,
    const QList<QString> *lst) {
  self->setRequiredFormats(*lst);
}

//  const QStringList &QSvgNode::requiredFormats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QSvgNode15requiredFormatsEv(
    const QSvgNode *self) {
  return new QList<QString>(self->requiredFormats());
}

//  void QSvgNode::setRequiredFonts(const QStringList &lst)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode16setRequiredFontsERK5QListI7QStringE(
    QSvgNode *self,
    const QList<QString> *lst) {
  self->setRequiredFonts(*lst);
}

//  const QStringList &QSvgNode::requiredFonts() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK8QSvgNode13requiredFontsEv(const QSvgNode *self) {
  return new QList<QString>(self->requiredFonts());
}

//  void QSvgNode::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode10setVisibleEb(QSvgNode *self, bool visible) {
  self->setVisible(visible);
}

//  bool QSvgNode::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode9isVisibleEv(const QSvgNode *self) {
  return self->isVisible();
}

//  void QSvgNode::setDisplayMode(DisplayMode display)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode14setDisplayModeENS_11DisplayModeE(
    QSvgNode *self,
    QSvgNode::DisplayMode display) {
  self->setDisplayMode(display);
}

//  DisplayMode QSvgNode::displayMode() const
extern "C" Q_DECL_EXPORT
QSvgNode::DisplayMode ritual_ZNK8QSvgNode11displayModeEv(
    const QSvgNode *self) {
  return self->displayMode();
}

//  QString QSvgNode::nodeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode6nodeIdEv(const QSvgNode *self) {
  return new QString(self->nodeId());
}

//  void QSvgNode::setNodeId(const QString &i)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode9setNodeIdERK7QString(
    QSvgNode *self,
    const QString *i) {
  self->setNodeId(*i);
}

//  QString QSvgNode::xmlClass() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode8xmlClassEv(const QSvgNode *self) {
  return new QString(self->xmlClass());
}

//  void QSvgNode::setXmlClass(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode11setXmlClassERK7QString(
    QSvgNode *self,
    const QString *str) {
  self->setXmlClass(*str);
}

//  QString QSvgNode::maskId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode6maskIdEv(const QSvgNode *self) {
  return new QString(self->maskId());
}

//  void QSvgNode::setMaskId(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode9setMaskIdERK7QString(
    QSvgNode *self,
    const QString *str) {
  self->setMaskId(*str);
}

//  bool QSvgNode::hasMask() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode7hasMaskEv(const QSvgNode *self) {
  return self->hasMask();
}

//  QString QSvgNode::filterId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode8filterIdEv(const QSvgNode *self) {
  return new QString(self->filterId());
}

//  void QSvgNode::setFilterId(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode11setFilterIdERK7QString(
    QSvgNode *self,
    const QString *str) {
  self->setFilterId(*str);
}

//  bool QSvgNode::hasFilter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode9hasFilterEv(const QSvgNode *self) {
  return self->hasFilter();
}

//  QString QSvgNode::markerStartId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode13markerStartIdEv(const QSvgNode *self) {
  return new QString(self->markerStartId());
}

//  void QSvgNode::setMarkerStartId(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode16setMarkerStartIdERK7QString(
    QSvgNode *self,
    const QString *str) {
  self->setMarkerStartId(*str);
}

//  bool QSvgNode::hasMarkerStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode14hasMarkerStartEv(const QSvgNode *self) {
  return self->hasMarkerStart();
}

//  QString QSvgNode::markerMidId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode11markerMidIdEv(const QSvgNode *self) {
  return new QString(self->markerMidId());
}

//  void QSvgNode::setMarkerMidId(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode14setMarkerMidIdERK7QString(
    QSvgNode *self,
    const QString *str) {
  self->setMarkerMidId(*str);
}

//  bool QSvgNode::hasMarkerMid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode12hasMarkerMidEv(const QSvgNode *self) {
  return self->hasMarkerMid();
}

//  QString QSvgNode::markerEndId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QSvgNode11markerEndIdEv(const QSvgNode *self) {
  return new QString(self->markerEndId());
}

//  void QSvgNode::setMarkerEndId(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode14setMarkerEndIdERK7QString(
    QSvgNode *self,
    const QString *str) {
  self->setMarkerEndId(*str);
}

//  bool QSvgNode::hasMarkerEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode12hasMarkerEndEv(const QSvgNode *self) {
  return self->hasMarkerEnd();
}

//  bool QSvgNode::hasAnyMarker() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode12hasAnyMarkerEv(const QSvgNode *self) {
  return self->hasAnyMarker();
}

//  bool QSvgNode::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgNode22requiresGroupRenderingEv(const QSvgNode *self) {
  return self->requiresGroupRendering();
}

//  QRectF QSvgNode::filterRegion(const QSvgDocument *doc, QRectF bounds)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QSvgNode12filterRegionEPK12QSvgDocument6QRectF(
    const QSvgNode *self,
    const QSvgDocument *doc,
    const QRectF *bounds) {
  return new QRectF(self->filterRegion(doc, *bounds));
}

//  qreal QSvgNode::strokeWidth(QPainter *p)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN8QSvgNode11strokeWidthEP8QPainter(QPainter *p) {
  return QSvgNode::strokeWidth(p);
}

//  void QSvgNode::initPainter(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgNode11initPainterEP8QPainter(QPainter *p) {
  QSvgNode::initPainter(p);
}

//  QRectF QSvgNode::boundsOnStroke(QPainter *p, const QPainterPath &path,
//      qreal width, BoundsMode mode)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN8QSvgNode14boundsOnStrokeEP8QPainterRK12QPainterPathdNS_10BoundsModeE(
    QPainter *p,
    const QPainterPath *path,
    qreal width,
    QSvgNode::BoundsMode mode) {
  return new QRectF(QSvgNode::boundsOnStroke(p, *path, width, mode));
}

//  a Python function taken by a CuteQSvgNode, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgNode(QSvgNode *self, const char *key, void *call) {
  return static_cast<CuteQSvgNode *>(self)->take(key, call);
}

//  bool QSvgNode::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgNode *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgNode::separateFillStroke(a0, *a1);
}

//  bool QSvgNode::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgNode22requiresGroupRenderingEv(
    const QSvgNode *self) {
  return self->QSvgNode::requiresGroupRendering();
}
