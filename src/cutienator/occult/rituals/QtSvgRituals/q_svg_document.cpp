//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgdocument_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <memory>
#include <QtCore/QString>
#include <QtCore/QFlags>
#include <QtCore/QByteArray>
#include <QtCore/QStringView>
#include <QtCore/QSharedPointer>

//  A QSvgDocument that Python can take functions over in. Every QSvgDocument
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgDocumentCall0)(const void *, int *);
typedef bool (*CuteQSvgDocumentCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgDocumentCall2)(const void *, int *);
class CuteQSvgDocument : public QSvgDocument {
public:
  using QSvgDocument::QSvgDocument;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgDocument::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgDocumentCall0 call = reinterpret_cast<CuteQSvgDocumentCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgDocument::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgDocumentCall1 call = reinterpret_cast<CuteQSvgDocumentCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgDocumentCall2 call = reinterpret_cast<CuteQSvgDocumentCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  std::unique_ptr<QSvgDocument> QSvgDocument::load(const QString &file,
//      QtSvg::Options options, QtSvg::AnimatorType type)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSvgDocument> *ritual_ZN12QSvgDocument4loadERK7QString6QFlagsIN5QtSvg6OptionEENS4_12AnimatorTypeE(
    const QString *file,
    int options,
    QtSvg::AnimatorType type) {
  return new std::unique_ptr<QSvgDocument>(
      QSvgDocument::load(
          *file,
          QFlags<QtSvg::Option>::fromInt(options),
          type));
}

//  std::unique_ptr<QSvgDocument> QSvgDocument::load(const QByteArray
//      &contents, QtSvg::Options options, QtSvg::AnimatorType type)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSvgDocument> *ritual_ZN12QSvgDocument4loadERK10QByteArray6QFlagsIN5QtSvg6OptionEENS4_12AnimatorTypeE(
    const QByteArray *contents,
    int options,
    QtSvg::AnimatorType type) {
  return new std::unique_ptr<QSvgDocument>(
      QSvgDocument::load(
          *contents,
          QFlags<QtSvg::Option>::fromInt(options),
          type));
}

//  std::unique_ptr<QSvgDocument> QSvgDocument::load(QXmlStreamReader
//      *contents, QtSvg::Options options, QtSvg::AnimatorType type)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QSvgDocument> *ritual_ZN12QSvgDocument4loadEP16QXmlStreamReader6QFlagsIN5QtSvg6OptionEENS3_12AnimatorTypeE(
    QXmlStreamReader *contents,
    int options,
    QtSvg::AnimatorType type) {
  return new std::unique_ptr<QSvgDocument>(
      QSvgDocument::load(
          contents,
          QFlags<QtSvg::Option>::fromInt(options),
          type));
}

//  bool QSvgDocument::isLikelySvg(QIODevice *device, bool *isCompressed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSvgDocument11isLikelySvgEP9QIODevicePb(
    QIODevice *device,
    bool *isCompressed) {
  return QSvgDocument::isLikelySvg(device, isCompressed);
}

//  QSvgDocument::QSvgDocument(QtSvg::Options options, QtSvg::AnimatorType
//      type)
extern "C" Q_DECL_EXPORT
QSvgDocument *ritual_ZN12QSvgDocumentC1E6QFlagsIN5QtSvg6OptionEENS1_12AnimatorTypeE(
    int options,
    QtSvg::AnimatorType type) {
  return new CuteQSvgDocument(QFlags<QtSvg::Option>::fromInt(options), type);
}

//  QSvgDocument::~QSvgDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocumentD1Ev(QSvgDocument *self) {
  delete self;
}

//  Type QSvgDocument::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK12QSvgDocument4typeEv(const QSvgDocument *self) {
  return self->type();
}

//  QSize QSvgDocument::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QSvgDocument4sizeEv(const QSvgDocument *self) {
  return new QSize(self->size());
}

//  void QSvgDocument::setWidth(int len, bool percent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument8setWidthEib(
    QSvgDocument *self,
    int len,
    bool percent) {
  self->setWidth(len, percent);
}

//  void QSvgDocument::setHeight(int len, bool percent)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument9setHeightEib(
    QSvgDocument *self,
    int len,
    bool percent) {
  self->setHeight(len, percent);
}

//  int QSvgDocument::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgDocument5widthEv(const QSvgDocument *self) {
  return self->width();
}

//  int QSvgDocument::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgDocument6heightEv(const QSvgDocument *self) {
  return self->height();
}

//  bool QSvgDocument::widthPercent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgDocument12widthPercentEv(const QSvgDocument *self) {
  return self->widthPercent();
}

//  bool QSvgDocument::heightPercent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgDocument13heightPercentEv(const QSvgDocument *self) {
  return self->heightPercent();
}

//  bool QSvgDocument::preserveAspectRatio() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgDocument19preserveAspectRatioEv(
    const QSvgDocument *self) {
  return self->preserveAspectRatio();
}

//  void QSvgDocument::setPreserveAspectRatio(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument22setPreserveAspectRatioEb(
    QSvgDocument *self,
    bool on) {
  self->setPreserveAspectRatio(on);
}

//  QRectF QSvgDocument::viewBox() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSvgDocument7viewBoxEv(const QSvgDocument *self) {
  return new QRectF(self->viewBox());
}

//  void QSvgDocument::setViewBox(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument10setViewBoxERK6QRectF(
    QSvgDocument *self,
    const QRectF *rect) {
  self->setViewBox(*rect);
}

//  bool QSvgDocument::isCalculatingImplicitViewBox() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgDocument28isCalculatingImplicitViewBoxEv(
    const QSvgDocument *self) {
  return self->isCalculatingImplicitViewBox();
}

//  QtSvg::Options QSvgDocument::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgDocument7optionsEv(const QSvgDocument *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QSvgDocument::drawCommand(QPainter *a0, QSvgExtraStates &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgDocument *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  self->drawCommand(a0, *a1);
}

//  void QSvgDocument::draw(QPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument4drawEP8QPainter(
    QSvgDocument *self,
    QPainter *p) {
  self->draw(p);
}

//  void QSvgDocument::draw(QPainter *p, const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument4drawEP8QPainterRK6QRectF(
    QSvgDocument *self,
    QPainter *p,
    const QRectF *bounds) {
  self->draw(p, *bounds);
}

//  void QSvgDocument::draw(QPainter *p, const QString &id, const QRectF
//      &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument4drawEP8QPainterRK7QStringRK6QRectF(
    QSvgDocument *self,
    QPainter *p,
    const QString *id,
    const QRectF *bounds) {
  self->draw(p, *id, *bounds);
}

//  QTransform QSvgDocument::transformForElement(const QString &id) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK12QSvgDocument19transformForElementERK7QString(
    const QSvgDocument *self,
    const QString *id) {
  return new QTransform(self->transformForElement(*id));
}

//  QRectF QSvgDocument::boundsOnElement(const QString &id) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK12QSvgDocument15boundsOnElementERK7QString(
    const QSvgDocument *self,
    const QString *id) {
  return new QRectF(self->boundsOnElement(*id));
}

//  bool QSvgDocument::elementExists(const QString &id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgDocument13elementExistsERK7QString(
    const QSvgDocument *self,
    const QString *id) {
  return self->elementExists(*id);
}

//  QSvgFont *QSvgDocument::svgFont(const QString &family) const
extern "C" Q_DECL_EXPORT
QSvgFont *ritual_ZNK12QSvgDocument7svgFontERK7QString(
    const QSvgDocument *self,
    const QString *family) {
  return self->svgFont(*family);
}

//  void QSvgDocument::addNamedNode(const QString &id, QSvgNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument12addNamedNodeERK7QStringP8QSvgNode(
    QSvgDocument *self,
    const QString *id,
    QSvgNode *node) {
  self->addNamedNode(*id, node);
}

//  QSvgNode *QSvgDocument::namedNode(const QString &id) const
extern "C" Q_DECL_EXPORT
QSvgNode *ritual_ZNK12QSvgDocument9namedNodeERK7QString(
    const QSvgDocument *self,
    const QString *id) {
  return self->namedNode(*id);
}

//  void QSvgDocument::addPaintServer(QSvgPaintServerSharedPtr paintServer,
//      const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument14addPaintServerESt10shared_ptrI15QSvgPaintServerERK7QString(
    QSvgDocument *self,
    const QSvgPaintServerSharedPtr *paintServer,
    const QString *id) {
  self->addPaintServer(*paintServer, *id);
}

//  QSvgPaintServerSharedPtr QSvgDocument::paintServer(QStringView id) const
extern "C" Q_DECL_EXPORT
QSvgPaintServerSharedPtr *ritual_ZNK12QSvgDocument11paintServerE11QStringView(
    const QSvgDocument *self,
    const QString *id) {
  return new QSvgPaintServerSharedPtr(self->paintServer(QStringView(*id)));
}

//  void QSvgDocument::restartAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument16restartAnimationEv(QSvgDocument *self) {
  self->restartAnimation();
}

//  qint64 QSvgDocument::currentElapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QSvgDocument14currentElapsedEv(const QSvgDocument *self) {
  return self->currentElapsed();
}

//  bool QSvgDocument::animated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgDocument8animatedEv(const QSvgDocument *self) {
  return self->animated();
}

//  void QSvgDocument::setAnimated(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument11setAnimatedEb(QSvgDocument *self, bool a) {
  self->setAnimated(a);
}

//  int QSvgDocument::animationDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgDocument17animationDurationEv(const QSvgDocument *self) {
  return self->animationDuration();
}

//  int QSvgDocument::currentFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSvgDocument12currentFrameEv(const QSvgDocument *self) {
  return self->currentFrame();
}

//  void QSvgDocument::setCurrentFrame(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument15setCurrentFrameEi(QSvgDocument *self, int a0) {
  self->setCurrentFrame(a0);
}

//  void QSvgDocument::setFramesPerSecond(int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument18setFramesPerSecondEi(
    QSvgDocument *self,
    int num) {
  self->setFramesPerSecond(num);
}

//  QSharedPointer<QSvgAbstractAnimator> QSvgDocument::animator() const
extern "C" Q_DECL_EXPORT
QSharedPointer<QSvgAbstractAnimator> *ritual_ZNK12QSvgDocument8animatorEv(
    const QSvgDocument *self) {
  return new QSharedPointer<QSvgAbstractAnimator>(self->animator());
}

//  void QSvgDocument::mapSourceToTarget(QPainter *p, const QRectF
//      &targetRect, const QRectF &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgDocument17mapSourceToTargetEP8QPainterRK6QRectFS4_(
    QSvgDocument *self,
    QPainter *p,
    const QRectF *targetRect,
    const QRectF *sourceRect) {
  self->mapSourceToTarget(p, *targetRect, *sourceRect);
}

//  a Python function taken by a CuteQSvgDocument, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgDocument(
    QSvgDocument *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgDocument *>(self)->take(key, call);
}

//  Type QSvgDocument::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK12QSvgDocument4typeEv(
    const QSvgDocument *self) {
  return self->QSvgDocument::type();
}

//  a std::unique_ptr<QSvgDocument> a ritual of QSvgDocument gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgDocument__std_unique_ptr_QSvgDocument(
    std::unique_ptr<QSvgDocument> *self) {
  delete self;
}

//  a QSvgPaintServerSharedPtr a ritual of QSvgDocument gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgDocument__QSvgPaintServerSharedPtr(
    QSvgPaintServerSharedPtr *self) {
  delete self;
}

//  a QSharedPointer<QSvgAbstractAnimator> a ritual of QSvgDocument gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgDocument__QSharedPointer_QSvgAbstractAnimator(
    QSharedPointer<QSvgAbstractAnimator> *self) {
  delete self;
}
