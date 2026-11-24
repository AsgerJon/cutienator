//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtextnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtextnode.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QSGTextNode that Python can take functions over in. Every QSGTextNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGTextNodeCall0)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGTextNodeCall1)(const void *, int *);
typedef void (*CuteQSGTextNodeCall2)(const void *, int, int *);
typedef int (*CuteQSGTextNodeCall3)(const void *, int *);
typedef void (*CuteQSGTextNodeCall4)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGTextNodeCall5)(const void *, int *);
typedef void (*CuteQSGTextNodeCall6)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGTextNodeCall7)(const void *, int *);
typedef void (*CuteQSGTextNodeCall8)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGTextNodeCall9)(const void *, int *);
typedef void (*CuteQSGTextNodeCall10)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGTextNodeCall11)(const void *, int *);
typedef void (*CuteQSGTextNodeCall12)(const void *, int, int *);
typedef int (*CuteQSGTextNodeCall13)(const void *, int *);
typedef void (*CuteQSGTextNodeCall14)(const void *, int, int *);
typedef int (*CuteQSGTextNodeCall15)(const void *, int *);
typedef void (*CuteQSGTextNodeCall16)(const void *, int, int *);
typedef int (*CuteQSGTextNodeCall17)(const void *, int *);
typedef void (*CuteQSGTextNodeCall18)(const void *, int *);
typedef void (*CuteQSGTextNodeCall19)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGTextNodeCall20)(const void *, int *);
typedef void (*CuteQSGTextNodeCall21)(const void *, const QPointF *, QTextLayout *, int, int, int, int, int *);
typedef void (*CuteQSGTextNodeCall22)(const void *, const QPointF *, QTextDocument *, int, int, int *);
typedef bool (*CuteQSGTextNodeCall23)(const void *, int *);
typedef void (*CuteQSGTextNodeCall24)(const void *, int *);
class CuteQSGTextNode : public QSGTextNode {
public:
  using QSGTextNode::QSGTextNode;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN11QSGTextNode8setColorE6QColor")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode5colorEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setTextStyleENS_9TextStyleE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode9textStyleEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode13setStyleColorE6QColor")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode10styleColorEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setLinkColorE6QColor")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode9linkColorEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode17setSelectionColorE6QColor")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode14selectionColorEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode21setSelectionTextColorE6QColor")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode18selectionTextColorEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode13setRenderTypeENS_10RenderTypeE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode10renderTypeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode20setRenderTypeQualityEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode17renderTypeQualityEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode9filteringEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode5clearEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode11setViewportERK6QRectF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode8viewportEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[24] = call;
      return true;
    }
    return false;
  }

  //  void QSGTextNode::setColor(QColor color)
  void setColor(QColor color) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTextNodeCall0 call = reinterpret_cast<CuteQSGTextNodeCall0>(taken[0]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  QColor QSGTextNode::color() const
  QColor color() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTextNodeCall1 call = reinterpret_cast<CuteQSGTextNodeCall1>(taken[1]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGTextNode::setTextStyle(TextStyle textStyle)
  void setTextStyle(QSGTextNode::TextStyle textStyle) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGTextNodeCall2 call = reinterpret_cast<CuteQSGTextNodeCall2>(taken[2]);
      call(this, static_cast<int>(textStyle), &handled);
      if (handled) return;
    }
  }

  //  TextStyle QSGTextNode::textStyle()
  QSGTextNode::TextStyle textStyle() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGTextNodeCall3 call = reinterpret_cast<CuteQSGTextNodeCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTextNode::TextStyle>(given);
    }
    return {};
  }

  //  void QSGTextNode::setStyleColor(QColor styleColor)
  void setStyleColor(QColor styleColor) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGTextNodeCall4 call = reinterpret_cast<CuteQSGTextNodeCall4>(taken[4]);
      call(this, &styleColor, &handled);
      if (handled) return;
    }
  }

  //  QColor QSGTextNode::styleColor() const
  QColor styleColor() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGTextNodeCall5 call = reinterpret_cast<CuteQSGTextNodeCall5>(taken[5]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGTextNode::setLinkColor(QColor linkColor)
  void setLinkColor(QColor linkColor) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGTextNodeCall6 call = reinterpret_cast<CuteQSGTextNodeCall6>(taken[6]);
      call(this, &linkColor, &handled);
      if (handled) return;
    }
  }

  //  QColor QSGTextNode::linkColor() const
  QColor linkColor() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGTextNodeCall7 call = reinterpret_cast<CuteQSGTextNodeCall7>(taken[7]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGTextNode::setSelectionColor(QColor selectionColor)
  void setSelectionColor(QColor selectionColor) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGTextNodeCall8 call = reinterpret_cast<CuteQSGTextNodeCall8>(taken[8]);
      call(this, &selectionColor, &handled);
      if (handled) return;
    }
  }

  //  QColor QSGTextNode::selectionColor() const
  QColor selectionColor() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGTextNodeCall9 call = reinterpret_cast<CuteQSGTextNodeCall9>(taken[9]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGTextNode::setSelectionTextColor(QColor selectionTextColor)
  void setSelectionTextColor(QColor selectionTextColor) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGTextNodeCall10 call = reinterpret_cast<CuteQSGTextNodeCall10>(taken[10]);
      call(this, &selectionTextColor, &handled);
      if (handled) return;
    }
  }

  //  QColor QSGTextNode::selectionTextColor() const
  QColor selectionTextColor() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGTextNodeCall11 call = reinterpret_cast<CuteQSGTextNodeCall11>(taken[11]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGTextNode::setRenderType(RenderType renderType)
  void setRenderType(QSGTextNode::RenderType renderType) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGTextNodeCall12 call = reinterpret_cast<CuteQSGTextNodeCall12>(taken[12]);
      call(this, static_cast<int>(renderType), &handled);
      if (handled) return;
    }
  }

  //  RenderType QSGTextNode::renderType() const
  QSGTextNode::RenderType renderType() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGTextNodeCall13 call = reinterpret_cast<CuteQSGTextNodeCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTextNode::RenderType>(given);
    }
    return {};
  }

  //  void QSGTextNode::setRenderTypeQuality(int renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGTextNodeCall14 call = reinterpret_cast<CuteQSGTextNodeCall14>(taken[14]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
  }

  //  int QSGTextNode::renderTypeQuality() const
  int renderTypeQuality() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGTextNodeCall15 call = reinterpret_cast<CuteQSGTextNodeCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGTextNode::setFiltering(QSGTexture::Filtering a0)
  void setFiltering(QSGTexture::Filtering a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGTextNodeCall16 call = reinterpret_cast<CuteQSGTextNodeCall16>(taken[16]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
  }

  //  QSGTexture::Filtering QSGTextNode::filtering() const
  QSGTexture::Filtering filtering() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGTextNodeCall17 call = reinterpret_cast<CuteQSGTextNodeCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return {};
  }

  //  void QSGTextNode::clear()
  void clear() override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGTextNodeCall18 call = reinterpret_cast<CuteQSGTextNodeCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGTextNode::setViewport(const QRectF &viewport)
  void setViewport(const QRectF &viewport) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGTextNodeCall19 call = reinterpret_cast<CuteQSGTextNodeCall19>(taken[19]);
      call(this, &viewport, &handled);
      if (handled) return;
    }
  }

  //  QRectF QSGTextNode::viewport() const
  QRectF viewport() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGTextNodeCall20 call = reinterpret_cast<CuteQSGTextNodeCall20>(taken[20]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGTextNode::doAddTextLayout(QPointF position, QTextLayout
  //      *layout, int selectionStart, int selectionCount, int lineStart,
  //      int lineCount)
  void doAddTextLayout(
      QPointF position,
      QTextLayout *layout,
      int selectionStart,
      int selectionCount,
      int lineStart,
      int lineCount) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGTextNodeCall21 call = reinterpret_cast<CuteQSGTextNodeCall21>(taken[21]);
      call(this, &position, layout, selectionStart, selectionCount, lineStart, lineCount, &handled);
      if (handled) return;
    }
  }

  //  void QSGTextNode::doAddTextDocument(QPointF position, QTextDocument
  //      *document, int selectionStart, int selectionCount)
  void doAddTextDocument(
      QPointF position,
      QTextDocument *document,
      int selectionStart,
      int selectionCount) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGTextNodeCall22 call = reinterpret_cast<CuteQSGTextNodeCall22>(taken[22]);
      call(this, &position, document, selectionStart, selectionCount, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGTextNodeCall23 call = reinterpret_cast<CuteQSGTextNodeCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGTextNodeCall24 call = reinterpret_cast<CuteQSGTextNodeCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGTextNode::~QSGTextNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNodeD1Ev(QSGTextNode *self) {
  delete self;
}

//  void QSGTextNode::setColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode8setColorE6QColor(
    QSGTextNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QSGTextNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSGTextNode5colorEv(const QSGTextNode *self) {
  return new QColor(self->color());
}

//  void QSGTextNode::setTextStyle(TextStyle textStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode12setTextStyleENS_9TextStyleE(
    QSGTextNode *self,
    QSGTextNode::TextStyle textStyle) {
  self->setTextStyle(textStyle);
}

//  TextStyle QSGTextNode::textStyle()
extern "C" Q_DECL_EXPORT
QSGTextNode::TextStyle ritual_ZN11QSGTextNode9textStyleEv(
    QSGTextNode *self) {
  return self->textStyle();
}

//  void QSGTextNode::setStyleColor(QColor styleColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode13setStyleColorE6QColor(
    QSGTextNode *self,
    const QColor *styleColor) {
  self->setStyleColor(*styleColor);
}

//  QColor QSGTextNode::styleColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSGTextNode10styleColorEv(const QSGTextNode *self) {
  return new QColor(self->styleColor());
}

//  void QSGTextNode::setLinkColor(QColor linkColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode12setLinkColorE6QColor(
    QSGTextNode *self,
    const QColor *linkColor) {
  self->setLinkColor(*linkColor);
}

//  QColor QSGTextNode::linkColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSGTextNode9linkColorEv(const QSGTextNode *self) {
  return new QColor(self->linkColor());
}

//  void QSGTextNode::setSelectionColor(QColor selectionColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode17setSelectionColorE6QColor(
    QSGTextNode *self,
    const QColor *selectionColor) {
  self->setSelectionColor(*selectionColor);
}

//  QColor QSGTextNode::selectionColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSGTextNode14selectionColorEv(const QSGTextNode *self) {
  return new QColor(self->selectionColor());
}

//  void QSGTextNode::setSelectionTextColor(QColor selectionTextColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode21setSelectionTextColorE6QColor(
    QSGTextNode *self,
    const QColor *selectionTextColor) {
  self->setSelectionTextColor(*selectionTextColor);
}

//  QColor QSGTextNode::selectionTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSGTextNode18selectionTextColorEv(
    const QSGTextNode *self) {
  return new QColor(self->selectionTextColor());
}

//  void QSGTextNode::setRenderType(RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode13setRenderTypeENS_10RenderTypeE(
    QSGTextNode *self,
    QSGTextNode::RenderType renderType) {
  self->setRenderType(renderType);
}

//  RenderType QSGTextNode::renderType() const
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_ZNK11QSGTextNode10renderTypeEv(
    const QSGTextNode *self) {
  return self->renderType();
}

//  void QSGTextNode::setRenderTypeQuality(int renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode20setRenderTypeQualityEi(
    QSGTextNode *self,
    int renderTypeQuality) {
  self->setRenderTypeQuality(renderTypeQuality);
}

//  int QSGTextNode::renderTypeQuality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGTextNode17renderTypeQualityEv(const QSGTextNode *self) {
  return self->renderTypeQuality();
}

//  void QSGTextNode::setFiltering(QSGTexture::Filtering a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode12setFilteringEN10QSGTexture9FilteringE(
    QSGTextNode *self,
    QSGTexture::Filtering a0) {
  self->setFiltering(a0);
}

//  QSGTexture::Filtering QSGTextNode::filtering() const
extern "C" Q_DECL_EXPORT
QSGTexture::Filtering ritual_ZNK11QSGTextNode9filteringEv(
    const QSGTextNode *self) {
  return self->filtering();
}

//  void QSGTextNode::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode5clearEv(QSGTextNode *self) {
  self->clear();
}

//  void QSGTextNode::setViewport(const QRectF &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode11setViewportERK6QRectF(
    QSGTextNode *self,
    const QRectF *viewport) {
  self->setViewport(*viewport);
}

//  QRectF QSGTextNode::viewport() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QSGTextNode8viewportEv(const QSGTextNode *self) {
  return new QRectF(self->viewport());
}

//  void QSGTextNode::addTextLayout(QPointF position, QTextLayout *layout,
//      int selectionStart, int selectionCount, int lineStart, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode13addTextLayoutE7QPointFP11QTextLayoutiiii(
    QSGTextNode *self,
    const QPointF *position,
    QTextLayout *layout,
    int selectionStart,
    int selectionCount,
    int lineStart,
    int lineCount) {
  self->addTextLayout(
      *position,
      layout,
      selectionStart,
      selectionCount,
      lineStart,
      lineCount);
}

//  void QSGTextNode::addTextDocument(QPointF position, QTextDocument
//      *document, int selectionStart, int selectionCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode15addTextDocumentE7QPointFP13QTextDocumentii(
    QSGTextNode *self,
    const QPointF *position,
    QTextDocument *document,
    int selectionStart,
    int selectionCount) {
  self->addTextDocument(*position, document, selectionStart, selectionCount);
}

//  void QSGTextNode::doAddTextLayout(QPointF position, QTextLayout *layout,
//      int selectionStart, int selectionCount, int lineStart, int lineCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii(
    QSGTextNode *self,
    const QPointF *position,
    QTextLayout *layout,
    int selectionStart,
    int selectionCount,
    int lineStart,
    int lineCount) {
  self->doAddTextLayout(
      *position,
      layout,
      selectionStart,
      selectionCount,
      lineStart,
      lineCount);
}

//  void QSGTextNode::doAddTextDocument(QPointF position, QTextDocument
//      *document, int selectionStart, int selectionCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii(
    QSGTextNode *self,
    const QPointF *position,
    QTextDocument *document,
    int selectionStart,
    int selectionCount) {
  self->doAddTextDocument(
      *position,
      document,
      selectionStart,
      selectionCount);
}

//  a Python function taken by a CuteQSGTextNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTextNode(
    QSGTextNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTextNode *>(self)->take(key, call);
}
