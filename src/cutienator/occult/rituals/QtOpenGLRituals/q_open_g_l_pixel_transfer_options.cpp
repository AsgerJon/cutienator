//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglpixeltransferoptions.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglpixeltransferoptions.h>

//  QOpenGLPixelTransferOptions::QOpenGLPixelTransferOptions()
extern "C" Q_DECL_EXPORT
QOpenGLPixelTransferOptions *ritual_ZN27QOpenGLPixelTransferOptionsC1Ev() {
  return new QOpenGLPixelTransferOptions();
}

//  QOpenGLPixelTransferOptions::QOpenGLPixelTransferOptions(const
//      QOpenGLPixelTransferOptions &a0)
extern "C" Q_DECL_EXPORT
QOpenGLPixelTransferOptions *ritual_ZN27QOpenGLPixelTransferOptionsC1ERKS_(
    const QOpenGLPixelTransferOptions *a0) {
  return new QOpenGLPixelTransferOptions(*a0);
}

//  QOpenGLPixelTransferOptions
//      &QOpenGLPixelTransferOptions::operator=(QOpenGLPixelTransferOptions
//      &&other)
extern "C" Q_DECL_EXPORT
QOpenGLPixelTransferOptions *ritual_ZN27QOpenGLPixelTransferOptionsaSEOS_(
    QOpenGLPixelTransferOptions *self,
    QOpenGLPixelTransferOptions *other) {
  return &(self->operator=(std::move(*other)));
}

//  QOpenGLPixelTransferOptions &QOpenGLPixelTransferOptions::operator=(const
//      QOpenGLPixelTransferOptions &a0)
extern "C" Q_DECL_EXPORT
QOpenGLPixelTransferOptions *ritual_ZN27QOpenGLPixelTransferOptionsaSERKS_(
    QOpenGLPixelTransferOptions *self,
    const QOpenGLPixelTransferOptions *a0) {
  return &(self->operator=(*a0));
}

//  QOpenGLPixelTransferOptions::~QOpenGLPixelTransferOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptionsD1Ev(
    QOpenGLPixelTransferOptions *self) {
  delete self;
}

//  void QOpenGLPixelTransferOptions::swap(QOpenGLPixelTransferOptions
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions4swapERS_(
    QOpenGLPixelTransferOptions *self,
    QOpenGLPixelTransferOptions *other) {
  self->swap(*other);
}

//  void QOpenGLPixelTransferOptions::setAlignment(int alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions12setAlignmentEi(
    QOpenGLPixelTransferOptions *self,
    int alignment) {
  self->setAlignment(alignment);
}

//  int QOpenGLPixelTransferOptions::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpenGLPixelTransferOptions9alignmentEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->alignment();
}

//  void QOpenGLPixelTransferOptions::setSkipImages(int skipImages)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions13setSkipImagesEi(
    QOpenGLPixelTransferOptions *self,
    int skipImages) {
  self->setSkipImages(skipImages);
}

//  int QOpenGLPixelTransferOptions::skipImages() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpenGLPixelTransferOptions10skipImagesEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->skipImages();
}

//  void QOpenGLPixelTransferOptions::setSkipRows(int skipRows)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions11setSkipRowsEi(
    QOpenGLPixelTransferOptions *self,
    int skipRows) {
  self->setSkipRows(skipRows);
}

//  int QOpenGLPixelTransferOptions::skipRows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpenGLPixelTransferOptions8skipRowsEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->skipRows();
}

//  void QOpenGLPixelTransferOptions::setSkipPixels(int skipPixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions13setSkipPixelsEi(
    QOpenGLPixelTransferOptions *self,
    int skipPixels) {
  self->setSkipPixels(skipPixels);
}

//  int QOpenGLPixelTransferOptions::skipPixels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpenGLPixelTransferOptions10skipPixelsEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->skipPixels();
}

//  void QOpenGLPixelTransferOptions::setImageHeight(int imageHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions14setImageHeightEi(
    QOpenGLPixelTransferOptions *self,
    int imageHeight) {
  self->setImageHeight(imageHeight);
}

//  int QOpenGLPixelTransferOptions::imageHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpenGLPixelTransferOptions11imageHeightEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->imageHeight();
}

//  void QOpenGLPixelTransferOptions::setRowLength(int rowLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions12setRowLengthEi(
    QOpenGLPixelTransferOptions *self,
    int rowLength) {
  self->setRowLength(rowLength);
}

//  int QOpenGLPixelTransferOptions::rowLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QOpenGLPixelTransferOptions9rowLengthEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->rowLength();
}

//  void QOpenGLPixelTransferOptions::setLeastSignificantByteFirst(bool
//      lsbFirst)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions28setLeastSignificantByteFirstEb(
    QOpenGLPixelTransferOptions *self,
    bool lsbFirst) {
  self->setLeastSignificantByteFirst(lsbFirst);
}

//  bool QOpenGLPixelTransferOptions::isLeastSignificantBitFirst() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpenGLPixelTransferOptions26isLeastSignificantBitFirstEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->isLeastSignificantBitFirst();
}

//  void QOpenGLPixelTransferOptions::setSwapBytesEnabled(bool swapBytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QOpenGLPixelTransferOptions19setSwapBytesEnabledEb(
    QOpenGLPixelTransferOptions *self,
    bool swapBytes) {
  self->setSwapBytesEnabled(swapBytes);
}

//  bool QOpenGLPixelTransferOptions::isSwapBytesEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QOpenGLPixelTransferOptions18isSwapBytesEnabledEv(
    const QOpenGLPixelTransferOptions *self) {
  return self->isSwapBytesEnabled();
}

#endif  // !defined(QT_NO_OPENGL)
